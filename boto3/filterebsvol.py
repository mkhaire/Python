#!/usr/bin/python3
'''
This script will filter EBS volumes with prod env Tag.
'''

import boto3
from pprint import pprint

session = boto3.session.Session(profile_name='default')
ec2 = session.client(service_name='ec2',region_name='us-east-1')

volid = []

response = ec2.describe_volumes(Filters=[{'Name': 'tag:Env', 'Values': ['Prod']}])

for each in response['Volumes']:
   volid.append((each['VolumeId']))
   print(volid)
