import boto3
import json

def backup_security_groups(input_file, region, output_file):
    ec2 = boto3.client('ec2', region_name=region)
    
    # Read Security Group IDs from the input file
    with open(input_file, 'r') as f:
        security_group_ids = [line.strip() for line in f if line.strip()]

    if not security_group_ids:
        print("No Security Group IDs found in the input file.")
        return

    print(f"Found {len(security_group_ids)} Security Group IDs in the file.")

    # Fetch details of the specified Security Groups
    response = ec2.describe_security_groups(GroupIds=security_group_ids)
    security_groups = response.get('SecurityGroups', [])
    
    if not security_groups:
        print("No Security Groups found for the provided IDs!")
        return

    print(f"Backing up {len(security_groups)} Security Groups...")

    # Backup logic
    backup_data = []
    for sg in security_groups:
        backup_data.append({
            "GroupId": sg['GroupId'],
            "GroupName": sg['GroupName'],
            "Description": sg['Description'],
            "VpcId": sg.get('VpcId'),
            "InboundRules": sg['IpPermissions'],
            "OutboundRules": sg['IpPermissionsEgress'],
            "Tags": sg.get('Tags', [])
        })

    # Save backup to file
    with open(output_file, 'w') as f:
        json.dump(backup_data, f, indent=4)

    print(f"Backup completed successfully! File saved to {output_file}")

# Usage example
# Replace 'security_group_ids.txt', 'us-west-2', and 'security_groups_backup.json' with your values
input_file = 'security_group_ids.txt'  # File containing Security Group IDs
region = 'us-east-1'                  # AWS Region
output_file = 'security_groups_backup.json'  # Output backup file

backup_security_groups(input_file, region, output_file)
