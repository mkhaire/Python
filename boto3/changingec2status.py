#!/usr/bin/python3
# This script takes user input for changing EC2 instance status.Using instance id as attribute in client object.
# Waiter object is use for waiting until reach required state.
import boto3
import sys

aws_con = boto3.session.Session(profile_name='default')
ec_con = aws_con.client(service_name='ec2', region_name='us-east-1')

while True:
    print("Use script to perform following actions on EC2 instance")
    print(" 1. Start \n 2. stop \n 3. Terminate \n 4. Exit")
    opt = int(input("Enter your option: "))
    if opt == 1:
        print("Starting EC2 instance")
        ec_con.start_instances(InstanceIds=['i-0c68eb4ea3ec78245'])
        waiter = ec_con.get_waiter('instance_running')
        waiter.wait(InstanceIds=['i-0c68eb4ea3ec78245'])
        print("Instance is started")
        sys.exit()
    elif opt == 2:
        print("Stopping EC2 instance")
        ec_con.stop_instances(InstanceIds=['i-0c68eb4ea3ec78245'])
        waiter = ec_con.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=['i-0c68eb4ea3ec78245'])
        print("Instance is stopped")
        sys.exit()
    elif opt == 3:
        print("Terminating EC2 instance")
        ec_con.terminate_instances(InstanceIds=['i-0c68eb4ea3ec78245'])
        waiter = ec_con.get_waiter('instance_terminated')
        waiter.wait(InstanceIds=['i-0c68eb4ea3ec78245'])
        print("Instance has been terminated")
        sys.exit()
    elif opt == 4:
        print("Exiting......")
        sys.exit()
    else:
        print("Invalid Option try again")

