#!/usr/bin/env python3

'''
    Description: python script to find the largest ineger from a given list of integers
'''
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
from sys import exit;

parser = ArgumentParser(description='Finding the largest integer number in a list', prog='largestNumber', usage='%(prog)s [option]')
parser.add_argument('-l','--list', action='store', type=int, dest='numbers', nargs='+', help='List of integers')
parser.add_argument('-v','--version', action='version', version='%(prog)s 0.01')

value = parser.parse_args()

if value.numbers is None:
   parser.print_help()
   exit()

def largest (insertList):
    large = 0
    for ELEMENT in insertList:
        if insertList[large] < ELEMENT:
            large = insertList.index(ELEMENT)
    return large

LARGEST = largest(value.numbers)

print("The largest number in the input list is {}".format(value.numbers[LARGEST]))
