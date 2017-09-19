#!/bin/env python

 def atomic_move(self, src, dest, unsafe_writes=False):
        '''atomically move src to dest, copying attributes from dest, returns true on success
        it uses os.rename to ensure this as it is an atomic operation, rest of the function is
        to work around limitations, corner cases and ensure selinux context is saved if possible'''
        context = None
        dest_stat = None
        b_src = to_bytes(src, errors='surrogate_or_strict')
        b_dest = to_bytes(dest, errors='surrogate_or_strict')
        if os.path.exists(b_dest):
            try:
                dest_stat = os.stat(b_dest)

                # copy mode and ownership
                os.chmod(b_src, dest_stat.st_mode & PERM_BITS)
                os.chown(b_src, dest_stat.st_uid, dest_stat.st_gid)

                # try to copy flags if possible
                if hasattr(os, 'chflags') and hasattr(dest_stat, 'st_flags'):
                    try:
                        os.chflags(b_src, dest_stat.st_flags)
                    except OSError as e:
                        for err in 'EOPNOTSUPP', 'ENOTSUP':
                            if hasattr(errno, err) and e.errno == getattr(errno, err):
                                break
                        else:
                            raise
            except OSError as e:
                if e.errno != errno.EPERM:
                    raise
            if self.selinux_enabled():
                context = self.selinux_context(dest)
        else:
                        if self.selinux_enabled():
                context = self.selinux_default_context(dest)

        creating = not os.path.exists(b_dest)

        try:
            # Optimistically try a rename, solves some corner cases and can avoid useless work, throws exception if not atomic.
            os.rename(b_src, b_dest)
        except (IOError, OSError) as e:
            if e.errno not in [errno.EPERM, errno.EXDEV, errno.EACCES, errno.ETXTBSY, errno.EBUSY]:
                # only try workarounds for errno 18 (cross device), 1 (not permitted),  13 (permission denied)
                # and 26 (text file busy) which happens on vagrant synced folders and other 'exotic' non posix file systems
                self.fail_json(msg='Could not replace file: %s to %s: %s' % (src, dest, to_native(e)),
                               exception=traceback.format_exc())
            else:
                b_dest_dir = os.path.dirname(b_dest)
                # Use bytes here.  In the shippable CI, this fails with
                # a UnicodeError with surrogateescape'd strings for an unknown
                # reason (doesn't happen in a local Ubuntu16.04 VM)
                native_dest_dir = b_dest_dir
                native_suffix = os.path.basename(b_dest)
                native_prefix = b('.ansible_tmp')
                error_msg = None
                tmp_dest_name = None
                try:
                    tmp_dest_fd, tmp_dest_name = tempfile.mkstemp(prefix=native_prefix, dir=native_dest_dir, suffix=native_suffix)
                except (OSError, IOError) as e:
                    error_msg = 'The destination directory (%s) is not writable by the current user. Error was: %s' % (os.path.dirname(dest), to_native(e))
                except TypeError:
                    # We expect that this is happening because python3.4.x and
                    # below can't handle byte strings in mkstemp().  Traceback
                    # would end in something like:
                    #     file = _os.path.join(dir, pre + name + suf)
                    # TypeError: can't concat bytes to str
                    error_msg = ('Failed creating temp file for atomic move.  This usually happens when using Python3 less than Python3.5. '
                                 'Please use Python2.x or Python3.5 or greater.')
                finally:
                    if error_msg:
                        if unsafe_writes:
                            self._unsafe_writes(b_src, b_dest)
                        else:
                            self.fail_json(msg=error_msg, exception=traceback.format_exc())

                if tmp_dest_name:
                    b_tmp_dest_name = to_bytes(tmp_dest_name, errors='surrogate_or_strict')

                    try:
                        try:
                            # close tmp file handle before file operations to prevent text file busy errors on vboxfs synced folders (windows host)
                            os.close(tmp_dest_fd)
                            # leaves tmp file behind when sudo and not root
                            try:
                                shutil.move(b_src, b_tmp_dest_name)
                            except OSError:
                                # cleanup will happen by 'rm' of tempdir
                                # copy2 will preserve some metadata
                                shutil.copy2(b_src, b_tmp_dest_name)

                            if self.selinux_enabled():
                                self.set_context_if_different(
                                    b_tmp_dest_name, context, False)
                            try:
                                tmp_stat = os.stat(b_tmp_dest_name)
                                if dest_stat and (tmp_stat.st_uid != dest_stat.st_uid or tmp_stat.st_gid != dest_stat.st_gid):
                                    os.chown(b_tmp_dest_name, dest_stat.st_uid, dest_stat.st_gid)
                            except OSError as e:
                                if e.errno != errno.EPERM:
                                    raise
                            try:
                                os.rename(b_tmp_dest_name, b_dest)
                            except (shutil.Error, OSError, IOError) as e:
                                if unsafe_writes and e.errno == errno.EBUSY:
                                    self._unsafe_writes(b_tmp_dest_name, b_dest)
                                else:
                                    self.fail_json(msg='Unable to rename file: %s to %s: %s' % (src, dest, to_native(e)),
                                                   exception=traceback.format_exc())
                        except (shutil.Error, OSError, IOError) as e:
                            self.fail_json(msg='Failed to replace file: %s to %s: %s' % (src, dest, to_native(e)),
                                           exception=traceback.format_exc())
                    finally:
                        self.cleanup(b_tmp_dest_name)
