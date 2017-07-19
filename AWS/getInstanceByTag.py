#!/bin/env python

import boto3 
import sys
Region = sys.argv[1]
Tag = sys.argv[2]

client = boto3.client('ec2',Region)
response = client.describe_instances(Filters=[{'Name':'tag:'+Tag,'Values':['nitanka-test']}])

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['State']['Name'])
        print(instance['PublicIpAddress'] + '  :  ' + instance['PrivateIpAddress'])
