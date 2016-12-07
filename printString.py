#!/usr/bin/env python3

# python script which will accept a string from the user and print the string
# to print the string it will call a function called printString() which
# will take a string as an argument and that string will be printed.

def printString(string):
    print ("The input string is : {}".format(string))


inputString = input("Please enter the string :    ")

# calling the function to call the printString to print the string

printString(inputString)


