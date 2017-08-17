#!/usr/bin/env python3 

'''
    Description:
       Python script to find the index of a word in a sentence

NOTE: This script will return wrong index number when the number of spaces between the words
#       are more than 1.

'''


from sys import exit
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter

parser = ArgumentParser(description='Find the index of a substring in a string', 
                       prog='findIndexofWord', 
                       usage='%(prog)s [option]')

parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.01')
parser.add_argument('--string', '-s', action='store', dest='string', type=str, help='String having the possible word')
parser.add_argument('--substring','-b', action='store', dest='word', type=str, help='Word for getting the index in string')

value = parser.parse_args()

if (value.string and value.word) is None:
   parser.print_help()
   exit()


def stringIndex(string,substring):
    stringIndex = 0 #Used for getting the current index count
    substringIndex = 0 #Used for matching while traversing
    substring = list(value.word) #Converting to list, for character to character matching
    
    for char in string:
        stringIndex += 1
        if substringIndex < len(substring) and char == substring[substringIndex]:
           substringIndex += 1
           if substringIndex == len(substring) and (stringIndex - substringIndex == 0) and string[stringIndex] == ' ':
               print('match')
               exit()

           if substringIndex == len(substring) and stringIndex < len(string) and stringIndex - substringIndex > 0:
                if string[stringIndex - substringIndex - 1] == ' ' and string[stringIndex] == ' ':
                    print('match')
                    exit()

           if substringIndex == len(substring) and stringIndex == len(string) and string[stringIndex - substringIndex - 1] == ' ':
                print('match')
                exit()
        else:
           substringIndex = 0          



stringIndex(value.string,value.word)
