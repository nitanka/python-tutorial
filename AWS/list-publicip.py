import boto3

ec2 = boto3.client('ec2','us-west-2')
filters = [{'Name': 'tag:Name', 'Values': ['cassandra']}]
response = ec2.describe_instances(Filters=filters)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        if instance['State']['Name'] == 'running': 
            print(instance['PublicIpAddress']) # + '  :  ' + instance['PrivateIpAddress']  )
        #print(instance['BlockDeviceMappings'])
        #print( 50 * '*')  #+ ':'  +   instance['PrivateIpAddress'])  #PublicIpAddress
