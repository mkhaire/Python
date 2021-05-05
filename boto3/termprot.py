#!/usr/bin/python3
#Enable Termination protection for all instances in a region

import boto3

aws_con = boto3.session.Session(profile_name='cloud_user')
ec2_con = aws_con.client(service_name='ec2',region_name='us-east-1')

response = ec2_con.describe_instances()['Reservations']

my_list = []

for each in response:
    for ec2 in each['Instances']:
        my_list.append(ec2['InstanceId'])
        
for prot in my_list: 
    ec2_con.modify_instance_attribute(DisableApiTermination={ 'Value': True }, InstanceId=prot)


