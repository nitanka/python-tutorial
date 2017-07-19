import boto3

ec2 = boto3.client('ec2','us-west-2')
filters = [{'Name': 'tag:name', 'Values': ['Reliance Test spark']}]
response = ec2.describe_instances(Filters=filters)
#print(response['Reservations'])

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        
        print(instance['PublicIpAddress'])   #+ '  :  ' + instance['PrivateIpAddress']  )
        #print(instance['BlockDeviceMappings'])
        #print( 50 * '*')  #+ ':'  +   instance['PrivateIpAddress'])  #PublicIpAddress
