#!/usr/bin/python3

import boto3
import sys
from random import choice

def iam_client_obj():
    session=boto3.session.Session(profile_name='cloud_user')
    iam_client=session.client(service_name='iam',region_name='us-east-1')
    return iam_client

def main():
    iam_client=iam_client_obj()
    iam_user_name=input("Enter IAM user name that needs to create: ")
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam_client.create_user(UserName=iam_user_name)
    except Exception as e:
        print(e)
        sys.exit(0)
    response = iam_client.create_access_key(UserName=iam_user_name)
    print("Print IAM Username={}".format(iam_user_name))
    print("AccessKeyId={}\nSecretAccessKey={}".format(response['AccessKey']['AccessKeyId'],response['AccessKey']['SecretAccessKey']))
    iam_client.attach_user_policy(UserName=iam_user_name,PolicyArn=PolicyArn)
    return None

if __name__=="__main__":
    main()
