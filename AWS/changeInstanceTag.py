#!/bin/env python

#Python script to change the tag of the instances

import boto3
import sys

def changeInstanceTag(region,tag,oldtagvalue,newtagvalue): 

    Region = region
    Tag = tag
    oldTagValue = oldtagvalue.split()
    newTagValue = newtagvalue

    ec2 = boto3.client('ec2', Region)
    response = ec2.describe_instances(Filters=[{ 'Name':'tag:'+ Tag,'Values': oldTagValue }])

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            ec2.create_tags( Resources=[instance['InstanceId']],Tags=[{ 'Key': Tag, 'Value': newTagValue }] )


Region = sys.argv[1] 
Tag = sys.argv[2]
oldTagValue = sys.argv[3]
newTagValue = sys.argv[4]

changeInstanceTag(Region,Tag,oldTagValue,newTagValue)
