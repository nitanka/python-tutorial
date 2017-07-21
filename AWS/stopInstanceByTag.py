#!/bin/env python

######################################################
# 						     #
# To stop the instances based on the instance tag    #
#						     #
######################################################

import boto3
import sys


def stopInstanceByTag(region,tag,tagvalue):
    Region = region
    Tag = tag
    tagValue = tagvalue.split()

    ec2 = boto3.client('ec2',Region)
    response = ec2.describe_instances(Filters=[{'Name':'tag:'+Tag,'Values':tagValue}])

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'running':
                ec2.stop_instances(InstanceIds=[instance['InstanceId']])


Region = sys.argv[1]
Tag = sys.argv[2]
tagValue = sys.argv[3]

stopInstanceByTag(Region,Tag,tagValue)

