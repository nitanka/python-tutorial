#!/bin/env python

#Python script to change the tag of the instances

import boto3
import sys

Region = sys.argv[1]
Tag = sys.argv[2]
oldTagValue = sys.argv[3].split()
newTagValue = sys.argv[4]

ec2 = boto3.client('ec2', Region)
response = ec2.describe_instances(Filters=[{ 'Name':'tag:'+ Tag,'Values': oldTagValue }])

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        ec2.create_tags( Resources=[instance['InstanceId']],Tags=[{ 'Key': Tag, 'Value': newTagValue }] )
   
