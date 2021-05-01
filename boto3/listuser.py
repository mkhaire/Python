#Listing IAM Users using resource object
import boto3
aws_man_con=boto3.session.Session(profile_name="cloud_user")
iam_resource=aws_man_con.resource('iam')

for users in iam_resource.users.all():
    print(users.name)


print("=====================")
#Listing IAM users using client object

iam_client=aws_man_con.client('iam')

for users in iam_client.list_users()['Users']:
    print(users['UserName'])

