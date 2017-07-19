import boto3    
ec2client = boto3.client('ec2',region_name='ap-northeast-1')
response = ec2client.describe_instances()
with open('./hosts', 'w') as infile:
    masters='[masters]'
    infile.write(masters)
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            if instance['State']['Name'] != 'terminated':
                print(instance['PublicIpAddress'])
                print("----------------")
                line = instance['PublicIpAddress'] + '\n'
                infile.write(line)



 
       # if instance['State']['Name'] != 'terminated': #State': {u'Code': 48, u'Name': 'terminated'}
       #    print(instance['PublicIpAddress'])
        #   with open('./hosts', 'w') as infile:
       #      infile.write(instance['PublicIpAddress'])
