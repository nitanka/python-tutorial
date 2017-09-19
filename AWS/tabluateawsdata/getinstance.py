#!/bin/env python3 

'''
    Getting the argument from the user 

'''
if __name__ == '__main__':

    from argparse import ArgumentParser
    from argparse import RawTextHelpFormatter
    from sys import exit
    from fetchdate import getEc2Information
    from fetchdate import printParameter
    
    parser = ArgumentParser(description='Printing EC2 query information',
                           prog='ec2query',
                           usage='%(prog)s [option]')
    parser.add_argument('--version', '-V', action='version', version='%(prog)s 0.1')
    parser.add_argument('--tag', '-t', action='store', dest='TAG', type=str, help='query by tag')
    parser.add_argument('--state','-s', action='store', dest='STATE', type=str, help='query by state', nargs='*',choices=['running','stop'],default=['running','stop'])
    parser.add_argument('--vpc', '-v', action='store', dest='VPC', type=str, help='query by vpc')
    
    arguments = parser.parse_args()
    
    if (arguments.VPC or arguments.STATE or arguements.TAG) is None:
        parser.print_help()
        exit()
    
    
    INPUTS = getEc2Information('us-west-2b',VPC=arguments.VPC, STATE=arguments.STATE, TAG=arguments.TAG)
    
    printParameter(INPUTS)
    
    
    
