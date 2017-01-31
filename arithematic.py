#!/usr/bin/env python3

# python script containing four function:
#
#	addition(num1, num2) : Addition of two numbers
#	substraction(num1, num2) : Substraction of two numbers
#	multiplication(num1, num2): Multiplication of twon numbers
#	division(num1, num2) : Division of num1 by num2 if num2 > 0
#

from sys import exit


def addition(num1, num2):
    # return num1 + num2
    return num1 + num2

def substraction (num1, num2):
    # return num1 - num2
    return num1 - num2

def multiplication (num1, num2):
    # return num1 * num2
    return num1 * num2


def division (num1, num2):
    #if num2 != 0 retun num1/num2 otherwise 0
    if num2 != 0:
        return num1 // num2
    else:
        return 0


try:
    num1 = int(input("Enter the first number :  "))
except ValueError as ve:
    print ("Enter Integer Values ")
    exit()

try:
    num2 = int(input("Enter the second number :  "))
except ValueError as ve:
    print ("Enter Integer Values ")
    exit()

operation = input("Enter the operation to perform (ADD, SUB, MUL, DIV)  :  ").upper()

print(operation)

if operation not in ["ADD","SUB","MUL","DIV"]:
   print ("Please select one of ADD,SUB,MUL,DIV as operation")
elif operation == "ADD":
     print ("ADDITION : {}".format(addition(num1,num2)))
elif operation == "SUB":
     print("SUBSTRACTION : {}".format(substraction(num1,num2)))
elif operation == "MUL":
     print("MULTIPLICATION : {}".format(multiplication(num1,num2)))
else:
     print("DIVISION : {}".format(division(num1,num2)))




