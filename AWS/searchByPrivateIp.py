#!/bin/env python

import boto3
import sys


'''
     python searchByPrivateIp.py <AWS-Region> '[private-ip1, private-ip2]'

'''
Region = sys.argv[1]
IP = sys.argv[2].strip('[]').split(',')
 
ec2 = boto3.client('ec2',Region)

for host in IP:
    response = ec2.describe_instances(Filters=[{'Name':'instance-state-name', 'Values':['running']},{'Name':'private-ip-address', 'Values':[host]}])
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print (instance['PublicIpAddress'] + '  :  ' + instance['PrivateIpAddress'])







