import json
import boto3
from pprint import pprint

def lambda_handler(event, context):
    ec2 = boto3.client(service_name='ec2',region_name='us-east-1')
    volid = []
    response = ec2.describe_volumes(Filters=[{'Name': 'tag:Env', 'Values': ['Prod']}])
    for each in response['Volumes']:
        volid.append((each['VolumeId']))
    snapid = []
    for each in volid:
        snap = ec2.create_snapshot(Description='Snap with Lambda',VolumeId=each)
        snapid.append(each)
    print("Below are the snapshot Id \n ")
    print(snapid)
    return None
