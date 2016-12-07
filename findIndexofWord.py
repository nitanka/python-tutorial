#!/usr/bin/env python3 

# python script to find the index of a word in a sentence

from sys import exit


inputString = input("Enter the sentence :  ")
findString = input("Enter the word to find : ")
index = 0


if len(findString.split()) > 1:
    print("Please enter only one word!!!")

for eachWord in inputString.split():
    print("===== {} =====".format(eachWord))
    if findString == eachWord:
        print ("The word is present in the sentence at the index {}".format(index))
        exit()
    else:
        index += (len(eachWord) + 1)


print ("{} is not present in the sentence".format(findString))
