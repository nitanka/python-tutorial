#!/bin/env python

import boto3
import sys
'''
  python earchByHostName.py <AWS REGIONS> '[aws-hostname1, aws-hostname2]'

'''
Region = sys.argv[1]
hostnames = sys.argv[2].strip('[]').split(',')

#removing ip and - from the hostname
hostnames = [x.replace('-','.').replace('ip.','') for x in hostnames ]

ec2 = boto3.client('ec2',Region)


# describe_instances take only one ip address as list for the filter private-ip-address
# For all host in the list, we need to iterate through the list
for host in hostnames:

    response = ec2.describe_instances(Filters=[{'Name':'instance-state-name', 'Values':['running']}, {'Name':'private-ip-address', 'Values':[host]}])

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(instance['PublicIpAddress'] + '  :  ' + instance['PrivateIpAddress'])
