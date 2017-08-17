#!/usr/bin/env python3 

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
    '''
        Find the Index of string inside another string

        Parameters:

          string: The string where to search for the substring
          substring: The string, index of which should be obtain in the string

        Returns:
          
          If substring is present, print the index of the substring.
    '''

    stringIndex = 0 #Used for getting the current index count
    substringIndex = 0 #Used for matching while traversing
    substring = list(value.word) #Converting to list, for character to character matching
    
    for char in string:
        stringIndex += 1
        if substringIndex < len(substring) and char == substring[substringIndex]:
           substringIndex += 1
           #Condition to check the matching when the pattern is present in beginning of the string 
           if substringIndex == len(substring) and (stringIndex - substringIndex == 0) and string[stringIndex] == ' ':
               print('Pattern found is the location {}'.format(stringIndex - substringIndex))
               exit()

           #Condition to check the matching when the pattern is present at the middle of the string
           if substringIndex == len(substring) and stringIndex < len(string) and stringIndex - substringIndex > 0:
               if string[stringIndex - substringIndex - 1] == ' ' and string[stringIndex] == ' ':
                    print('Pattern found is the location {}'.format(stringIndex - substringIndex))
                    exit()

           #Condition to check the matching when the patter is present at the end of the string
           if substringIndex == len(substring) and stringIndex == len(string) and string[stringIndex - substringIndex - 1] == ' ':
               print('Pattern found is the location {}'.format(stringIndex - substringIndex))
               exit()
        else:
           substringIndex = 0          
        
        #Condition to check if pattern not found and remaining characters in string is less than characters in substring
        if substring == 0 and len(substring) > len(string) - stringIndex:
            break #print('Pattern not found')
    print('Pattern not found')	

stringIndex(value.string,value.word)
