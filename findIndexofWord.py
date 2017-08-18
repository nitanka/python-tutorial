#!/bin/env python3

'''
    Description:
       Python script to find the index of a word in a sentence
    Options:
   
       -s or --string                : String where to search for the pattern
       -b or --substring             : Substring to search in the string
       -v or --version               : Version of program
    Example:
    
       $ python3 findindexofWord.py -s 'Simple is better than complex' -b 'better'
       $ python3 findindexofWord.py -s "Special cases aren't special enough to break the rules." -b "cases aren't"
'''

from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
from sys import exit


parser = ArgumentParser(description='Find the index of a substring in a string', 
                       prog='findIndexofWord', 
                       usage='%(prog)s [option]')

parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.2')
parser.add_argument('--string', '-s', action='store', dest='string', type=str, help='String having the possible word')
parser.add_argument('--substring','-b', action='store', dest='word', type=str, help='Word for getting the index in string')

value = parser.parse_args()

if (value.string and value.word) is None:
   parser.print_help()
   exit()

string = value.string
substring = value.word

def stringIndex(string,substring):
    '''
        Find the Index of string inside another string
        Parameters:
          string: The string where to search for the substring
          substring: The string, index of which should be obtain in the string
        Returns:
          
          If substring is present, print the index of the substring.
    '''
    stringIndex = 0
    while stringIndex < len(string):
       
       #condition to check if the length pattern is greater than length of remaining string characters 
        if len(substring) > len(string) - stringIndex:
            exit()
        
        init = stringIndex
    
        #condition checking the pattern at the beginning adnd end of line
        if stringIndex != 0 and string[stringIndex - 1] != ' ':
            stringIndex += 1
            continue
    
        #Matching of pattern starts 
        substringIndex = 0
        while substringIndex < len(substring):
            if substring[substringIndex] == string[stringIndex]:
                stringIndex += 1
            else:
                break
            if (substringIndex == len(substring) - 1 ) and (stringIndex == len(string) or string[stringIndex] == ' '):
                print("Match found")
                print('Index is {}'.format(init))
                exit()
            substringIndex += 1
    
        stringIndex += 1

stringIndex(string,substring)               
