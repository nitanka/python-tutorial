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

        #Condition to check end of Index string if a character match is present 
        if len(substring) > substringIndex and (substring[substringIndex] == char): 
            substringIndex += 1 #Increasing the index for next substring character
        else:
            substringIndex = 0 #reset substring index to zero for matching with next word in the string
        #Condition to break the loop in case of a match is found
        if stringIndex == len(string) or string[stringIndex] == ' ' and substringIndex == len(substring):
            print('Index of the substring is  {}'.format(stringIndex - substringIndex))
            exit()
        if substringIndex == 0 and len(string) - stringIndex < len(substring):
            print('Word in not present in the string')
            exit()

stringIndex(value.string,value.word)
