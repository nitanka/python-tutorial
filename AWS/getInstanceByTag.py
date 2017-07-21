#!/bin/env python

import boto3 
import sys

def getInstanceByTag(region,tag,tagvalue):

    Region = region   
    Tag = tag 
    tagValue = tagvalue.split() 
    ec2 = boto3.client('ec2',Region)
    response = ec2.describe_instances(Filters=[{'Name':'tag:' + Tag,'Values':tagValue}])

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(instance['State']['Name'])
            print(instance['PublicIpAddress'] + '  :  ' + instance['PrivateIpAddress'])


Region = sys.argv[1]
Tag = sys.argv[2]
tagValue = sys.argv[3]

getInstanceByTag(Region,Tag,tagValue)

