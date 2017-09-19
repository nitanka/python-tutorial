#!/bin/env python

import sys
import boto3
import ast 

Region = sys.argv[1]
selectionTag = sys.argv[2]
selectionValue = sys.argv[3].split()
addTag = list(ast.literal_eval(sys.argv[4]))

ec2 = boto3.client('ec2',Region)
response = ec2.describe_instances(Filters=[{'Name':'tag:' + selectionTag, 'Values': selectionValue },{'Name':'instance-state-name', 'Value':['running']}])

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        #if instance['State']['Name'] == 'running':
           for tagDict in addTag:
               ec2.create_tags(Resources=[instance['InstanceId']], Tags=[{'Key': tagDict['Key'], 'Value': tagDict['Value']}])

