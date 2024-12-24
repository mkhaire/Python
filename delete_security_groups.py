import boto3

def delete_security_groups(group_ids_file, region):
    ec2 = boto3.client('ec2', region_name=region)

    # Read the Security Group IDs from the file
    with open(group_ids_file, 'r') as file:
        group_ids = [line.strip() for line in file if line.strip()]

    for group_id in group_ids:
        print(f"\nAttempting to delete Security Group: {group_id}")
        try:
            # Delete the security group
            ec2.delete_security_group(GroupId=group_id)
            print(f"Security Group {group_id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting Security Group {group_id}: {e}")

if __name__ == "__main__":
    # Path to the file containing Security Group IDs (one per line)
    group_ids_file = 'security_group_ids.txt'
    
    # Specify the AWS region
    region = input("Enter the AWS region (e.g., us-east-1): ").strip()

    # Confirm before proceeding
    confirm = input(f"You are about to delete Security Groups in the {region} region. Proceed? (yes/no): ").strip().lower()
    if confirm == 'yes':
        delete_security_groups(group_ids_file, region)
    else:
        print("Deletion aborted.")
