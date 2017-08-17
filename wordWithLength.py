#!/usr/bin/env python3 

'''
   Description: python script to find the length of each word and print the length of words.

   Options:
     
     -v or --version    : version of the program 

     -s or --string     : string containing the array of words 
'''

from prettytable import PrettyTable
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
from sys import exit

parser = ArgumentParser(description='Printing the length of each word in a string', prog='wordWithLength', usage='%(prog)s [option]')

parser.add_argument('-v','--version', action='version', version='%(prog)s 0.01')
parser.add_argument('-s','--string', action='store', dest='string', type=str, help='String containing the array of words')
value = parser.parse_args()

if value.string is None:
   parser.print_help()
   exit()

def wordcount(string):
    '''
        Get the length of each word in a string
       
        Parameters:
        
           string: Operand having the string 
        
        Returns:
       
           Table with words and length of each word
    '''

    stringLen = {} #dictionary to store the key for word with corresponding value for len

    count = 0
    for word in string.split(" "):
        if word in stringLen.keys():
            continue
        for char in word:
            count += 1
        stringLen[word] = count # stringlen[word] = length of word
        count = 0 #set to zero, to make the counting of next word to start from zero

    outputTable = PrettyTable(['Word', 'Length'])
    for key,value in stringLen.items():
        outputTable.add_row([key,value])
    print(outputTable)
    

wordcount(value.string)





   
