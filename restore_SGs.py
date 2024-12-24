import boto3
import json

def restore_security_groups(backup_file, group_ids, region):
    ec2 = boto3.client('ec2', region_name=region)
    
    # Load the backup file
    with open(backup_file, 'r') as f:
        backup_data = json.load(f)

    for group_id in group_ids:
        print(f"\nAttempting to restore Security Group: {group_id}")
        
        # Find the Security Group data in the backup file
        security_group_data = next((sg for sg in backup_data if sg['GroupId'] == group_id), None)
        
        if not security_group_data:
            print(f"Security Group with ID {group_id} not found in the backup. Skipping...")
            continue
        
        try:
            # Recreate the Security Group
            response = ec2.create_security_group(
                GroupName=security_group_data['GroupName'],
                Description=security_group_data['Description'],
                VpcId=security_group_data.get('VpcId')
            )
            new_group_id = response['GroupId']
            print(f"Security Group created with new ID: {new_group_id}")
            
            # Add Tags
            if security_group_data.get('Tags'):
                ec2.create_tags(
                    Resources=[new_group_id],
                    Tags=security_group_data['Tags']
                )
                print(f"Tags applied: {security_group_data['Tags']}")

            # Recreate Inbound Rules
            if security_group_data.get('InboundRules'):
                ec2.authorize_security_group_ingress(
                    GroupId=new_group_id,
                    IpPermissions=security_group_data['InboundRules']
                )
                print("Inbound rules restored.")

            # Recreate Outbound Rules
            if security_group_data.get('OutboundRules'):
                # Fetch current outbound rules to check for duplicates
                current_rules = ec2.describe_security_groups(GroupIds=[new_group_id])['SecurityGroups'][0]['IpPermissionsEgress']
                
                # Filter out any rules already present (to avoid duplicates)
                new_outbound_rules = []
                for rule in security_group_data['OutboundRules']:
                    if rule not in current_rules:
                        new_outbound_rules.append(rule)
                
                # Add only non-duplicate rules
                if new_outbound_rules:
                    try:
                        ec2.authorize_security_group_egress(
                            GroupId=new_group_id,
                            IpPermissions=new_outbound_rules
                        )
                        print("Outbound rules restored.")
                    except Exception as e:
                        print(f"Error restoring outbound rules for Security Group {group_id}: {e}")
                else:
                    print("No new outbound rules to restore (all rules already exist).")

            print(f"Security Group {group_id} restoration complete!")

        except Exception as e:
            print(f"Error restoring Security Group {group_id}: {e}")

# Usage example
if __name__ == "__main__":
    # Replace with your backup file path
    backup_file = 'security_groups_backup.json'
    # Read Security Group IDs from file
    with open('security_group_ids.txt', 'r') as f:
        group_ids = [line.strip() for line in f if line.strip()]
    # AWS region
    region = 'us-east-1'

    restore_security_groups(backup_file, group_ids, region)
