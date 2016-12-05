#!/usr/bin/env python3

# python script to find the length of an input word

word = input ("Please enter the word :  ")

count = 0 # to store the number of character in the word

for char in word:  # for each character in the word
    count += 1     # increment the count of the number of character

print ("The length of the word is {}".format(count))
