'''This module is for managing the creation of directories,
   managing the permissions and modes'''
from .fileexists import ifexists
from os import getcwd
from os import makedirs
from shutil import rmtree
from os import remove
from os.path import isdir
from os.path import join
from os import rename
def create(path,name):
    '''Function to create directory'''
    makedirs('/'.join((path,name))) if not ifexists(path,name) else print("File aleardy exists")


def delete(path,name):
    '''Function to delete file/directory'''
    try:
        if isdir(join(path,name)):
            rmtree(join(path,name))
        else:
            remove(join(path,name))
    except FileNotFoundError as e:
        print(e.strerror)


def chname(path,name,newname):
    '''Function to rename a file/directory'''
    try:
        rename(join(path,name),join(path,newname))
    except TypeError as e:
        print(e.strerror)
    except FileNotFoundError as e:
       print(e.strerror)

            
