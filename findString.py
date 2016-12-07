#!/usr/bin/env python3

# python script to find the a word among the words present in the input sentence

from sys import exit

inputString = input("Input the sentence :  ")
findString = input ("Input the word to find :  ")

if len(findString.split()) != 1:
    print("Please enter a single word!!!")
    exit()
else:
    for eachWord in inputString.split():
        if findString == eachWord:
            print("The word to find is present in the input sentence")


