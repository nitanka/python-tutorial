#!/usr/bin/env python3
from os.path import exists
from os import getcwd

def ifexists(path,filename):
    '''This is the function to find whether the file
        exists or not'''
    FILE = str.join('/',(path,filename))
    if not exists(FILE):
       return False
    return True


#ifexists(getcwd(),'directory.py')
