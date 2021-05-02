import boto3
aws_con = boto3.session.Session(profile_name='default')
ec2_con = aws_con.client(service_name='ec2', region_name='us-east-1')
vol = ec2_con.describe_volumes()['Volumes']

result = ec2_con.describe_instances()['Reservations']
print("=================================Instance information=============================================")
for ec2 in result:
    #    pprint(result)
    for item in ec2['Instances']:
        print("==================================================")
        print("The Architecture is {} \n Instance Id is: {} \n Public IP of the instance is: {} \n Launch time of the instance is {} \n ".format(item['Architecture'],item['InstanceId'],item['PublicIpAddress'],item['LaunchTime'].strftime("%Y-%M-%D")))

print("==================================Volume information===========================================")
for info in vol:
    for state in info['Attachments']:
        print("EBS Volume ids is: {} \n Attachment state is: {} \n Instance id is: {} \n ".format(state['VolumeId'],state['State'],state['InstanceId']))
