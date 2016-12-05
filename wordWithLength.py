#!/usr/bin/env python3 

# python script to find the length of each word and print the length of words.

string = input ("Enter the string :  ")

stringLen = {} #dictionary to store the key for word with corresponding value for len

count = 0 #will be used to find the length of key

# finding the length of each word in the string

for word in string.split(" "):
    for char in word:
        count += 1
    stringLen[word] = count # stringlen[word] = length of word
    count = 0 #set to zero, to make the counting of next word to start from zero


#Printing the dictionary containing the length of each word
print ("WORD\t\t\tLENGTH")
print ()
for key,value in stringLen.items():
    print("{}\t\t\t{}".format(key,value))







   
