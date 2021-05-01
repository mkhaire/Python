#!/usr/bin/python3

import boto3


aws_con=boto3.session.Session(profile_name='cloud_user',region_name='us-east-1')
ec2_cli=aws_con.client('ec2')
ec2_res=aws_con.resource('ec2')

#for instance in ec2_con.describe_instances(Filters=[{'Name': 'architecture','Values': ['x86_64']}]):
for instance in ec2_res.instances.all():
#    print(instance)
    print(
         "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
         instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
         )
     )

print('==========EC2 using Client Objet===========')
response=ec2_cli.describe_instances()
#print(response)
for instance in response['Reservations']:
    for each_instance in instance['Instances']:
        print(each_instance['InstanceId'])
    print('=======================')











