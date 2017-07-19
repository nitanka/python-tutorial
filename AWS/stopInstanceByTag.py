#!/bin/env python

######################################################
# 						     #
# To stop the instances based on the instance tag    #
#						     #
######################################################

import boto3
import sys

Region = sys.argv[1]
Tag = sys.argv[2]
tagValue = sys.argv[3].split()

ec2 = boto3.client('ec2',Region)
response = ec2.describe_instances(Filters=[{'Name':'tag:'+Tag,'Values':tagValue}])

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
       if instance['State']['Name'] == 'running':
          ec2.stop_instances(InstanceIds=[instance['InstanceId']])

