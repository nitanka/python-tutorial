#!/bin/env python

import boto3 
import sys

'''
Description : To list the running instances of an AWS region based on the Tag 
Command Line Arguments : 
  * REGION_NAME: name of the region
  * TAG_NAME: tag to use to filter
  * TAG_VALUES: value to use for searching
'''


Region = sys.argv[1]
Tag = sys.argv[2]
tagVALUE = sys.argv[3].split()

client = boto3.client('ec2',Region)
response = client.describe_instances(Filters=[{'Name':'tag:' + Tag,'Values':tagVALUE},{'Name':'instance-state-name', 'Values':['running']}])

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['PublicIpAddress']  + '  :  ' + instance['PrivateIpAddress'])
