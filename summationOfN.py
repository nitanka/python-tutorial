#!/usr/bin/env python3 

# python script to find the consecutive addition of N positive numbers

from sys import exit

try:
    number = int(input("Enter the value of N :  "))
except ValueError as ve:
    print(" Enter a positive integer value ")
    exit()

if number < 0:
    print ("Enter a positive number")
else:
    # Executing the formula to obtain the result of 1+2+3+......+N
    result = (number * (number + 1))/2

print ("The result is {}".format(result))
