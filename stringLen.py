#!/usr/bin/env python3

'''
    Description: Python script to find the length of an input word

    Parameters: 

        word: Word for which we need to find the length

    Examples:
     
        $ python3 stringLen.py -w 'original'
'''

from argparse import ArgumentParser 
from argparse import RawTextHelpFormatter
from sys import exit

parser = ArgumentParser(description='Script to find the length of a word', prog='stringLen', usage='%(prog)s [option]')
parser.add_argument('-w','--word', action='store', dest='word', help='Length of word to find')

value = parser.parse_args()

if value.word in None:
   parser.print_help()
   exit

def length(word):
  
    '''
       Find the length of the input word

       Parameter:
          word: Word, whose length need to find

       Return:
          length of the word 
    '''

    count = 0 # to store the number of character in the word

    for char in word:  # for each character in the word
        count += 1     # increment the count of the number of character

    print ("The length of the word {}".format(word)

length(value.word)


