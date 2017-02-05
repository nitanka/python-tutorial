#!/usr/bin/env python3

# python script to find the largest number from a given list of numbers

from sys import exit;

def largest (insertList):
    large = 0
    for ELEMENT in insertList:
        if insertList[large] < ELEMENT:
            large = insertList.index(ELEMENT)
    return large
    

# Obtaining total number of elements in the list
try:
    totalElements = int(input("Enter the total number of elements in the list :  "))
except ValueError as ve:
    print("Please enter integers")
    print("Program Exiting!!!!!!!!!!!")
    exit()

if totalElements <= 0:
    print("Please enter values greater than 0")
    print("Program Exiting!!!!!!!!!!!")
    exit()

inputList = [] #Empty list to hold the integer list given by the user
count = 0      # counter to use for obtaining list items from the user. counter >= totalElements

while count < totalElements:
    try:
        element = int(input("Enter the number {}  ".format(count + 1)))
    except ValueError as ve:
        print("Enter integer number")
        continue 
        
    inputList.append(element)
    count += 1


LARGEST = largest(inputList)

print("The largest number in the input list is {}".format(inputList[LARGEST]))
