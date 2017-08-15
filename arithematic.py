#!/usr/bin/env python3

'''
  Description:
    Python script to perform basic arithematic operation on two operands

  Options:
   
  -x or --x           : Option to obtain the first operand

  -y or --y           : Option to obtain the second operand

  -op or --op         : Option to obtain the operation to perform on the operands
                
                        Arguments: ADD, SUB, MUL, DIV
  
   -h or --help       : Print the help message
 
   -v or --version    : Print the version of the script

 
  Examples:
    $ python3 arithematic.py -x 12 -y 12 -op add

    $ python3 arithematic.py --x 12 --y 23 --op MUL
'''

from sys import exit
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter

parser = ArgumentParser(description='Python program to perform basic arithematic operations',
                         prog='arithematic', 
                         usage='%(prog)s [options]', formatter_class=RawTextHelpFormatter )

parser.add_argument('--version','-V', action='version', version='%(prog)s 1.0')
parser.add_argument('-x','--x', action='store', dest='num1',type=int, help='First operand' )
parser.add_argument('-y', '--y', action='store', dest='num2', type=int, help='Second operand' )
parser.add_argument('-op', '--op', action='store', dest='operation', nargs=1, choices=['add','ADD','sub','SUB','mul','MUL','div','DIV'], help='Operation to perform on the operand (ADD,SUB,MUL,DIV)')

value = parser.parse_args()

#Condition to validate the passing of the three arguments with the option
if (value.num1 and value.num2 and value.operation) is None:
   parser.print_help()
   exit()

def addition(num1, num2):
    '''
        Perform addition of two integers
       
        Parameters:
        
        num1  : First operand for the arithematic operation
        num2  : Second operand for the arithematic operations

        Returns:
       
        Integer summation of the two operands

    '''
    return num1 + num2

def substraction (num1, num2):
    '''
        Perform substraction of two integers
       
        Parameters:
        
        num1  : First operand for the arithematic operation
        num2  : Second operand for the arithematic operations

        Returns:
       
        Integer substraction of the two operands

    '''
    return num1 - num2

def multiplication (num1, num2):
    '''
        Perform multiplication of two integers
       
        Parameters:
        
        num1  : First operand for the arithematic operation
        num2  : Second operand for the arithematic operations

        Returns:
       
        Integer multiplication of the two operands

    '''
    return num1 * num2


def division (num1, num2):
    '''
        Perform division of two integers
       
        Parameters:
        
        num1  : First operand for the arithematic operation
        num2  : Second operand for the arithematic operations

        Returns:
        
        if second operand is 0 returns 0; otherwise returns integer division of the two operands
    '''

    if num2 != 0:
        return num1 // num2
    else:
        return 0


#Converting the list to string
operation = ''.join(value.operation).upper()

if operation == 'ADD':
     print ("ADDITION : {}".format(addition(value.num1,value.num2)))
elif operation == "SUB":
     print("SUBSTRACTION : {}".format(substraction(value.num1,value.num2)))
elif operation == "MUL":
     print("MULTIPLICATION : {}".format(multiplication(value.num1,value.num2)))
else:
     print("DIVISION : {}".format(division(value.num1,value.num2)))

