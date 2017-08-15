#!/usr/bin/env python3

# python script containing four function:
#
#	addition(num1, num2) : Addition of two numbers
#	substraction(num1, num2) : Substraction of two numbers
#	multiplication(num1, num2): Multiplication of twon numbers
#	division(num1, num2) : Division of num1 by num2 if num2 > 0
#

from sys import exit
from argparse import ArgumentParser

parser = ArgumentParser(description='Python program to perform basic arithematic operations', usage='%(prog)s [options]')

parser.add_argument('--version','-V', action='version', version='%(prog)s 1.0')
parser.add_argument('-x','--x', action='store', dest='num1',type=int, help='First operand' )
parser.add_argument('-y', '--y', action='store', dest='num2', type=int, help='Second operand' )
parser.add_argument('-op', '--op', action='store', dest='operation', help='Operation to perform on the operand (ADD,SUB,MUL,DIV)')
value = parser.parse_args()

if (value.num1 and value.num2 and value.operation) is None:
   parser.print_help()
   exit()

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


#try:
#    num1 = int(input("Enter the first number :  "))
#    num2 = int(input("Enter the second number :  "))
#except ValueError as ve:
#    print ("Enter Integer Values ")
#    exit()


#operation = input("Enter the operation to perform (ADD, SUB, MUL, DIV)  :  ").upper()
operation = value.operation.upper()
print(operation)

if operation not in ["ADD","SUB","MUL","DIV"]:
   print ("Please select one of ADD,SUB,MUL,DIV as operation")
elif operation == 'ADD':
     print ("ADDITION : {}".format(addition(value.num1,value.num2)))
elif operation == "SUB":
     print("SUBSTRACTION : {}".format(substraction(value.num1,value.num2)))
elif operation == "MUL":
     print("MULTIPLICATION : {}".format(multiplication(value.num1,value.num2)))
else:
     print("DIVISION : {}".format(division(value.num1,value.num2)))




