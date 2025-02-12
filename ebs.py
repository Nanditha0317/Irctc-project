import boto3
import csv

def fetch_ebs_volumes_csv(output_file="ebs_volumes.csv", region="us-east-1"):
    # Initialize AWS EC2 client
    ec2_client = boto3.client('ec2', region_name=region)

    try:
        # Fetch all EBS volumes
        response = ec2_client.describe_volumes()

        # Prepare CSV data
        volumes_data = []
        for volume in response['Volumes']:
            volumes_data.append([
                volume['VolumeId'],
                volume['State'],
                volume['Size'],
                volume['VolumeType'],
                volume['AvailabilityZone'],
                volume.get('Iops', 'N/A'),
                volume.get('Throughput', 'N/A'),
                volume.get('SnapshotId', 'N/A'),
                volume.get('Encrypted', False),
                ', '.join([tag['Value'] for tag in volume.get('Tags', [])]) if 'Tags' in volume else "No Tags"
            ])

        # CSV Header
        header = ["Volume ID", "State", "Size (GB)", "Type", "Availability Zone", "IOPS", "Throughput", "Snapshot ID", "Encrypted", "Tags"]

        # Write to CSV
        with open(output_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(volumes_data)

        print(f"EBS volumes data saved to {output_file}")

    except Exception as e:
        print(f"Error fetching EBS volumes: {e}")

# Call the function
fetch_ebs_volumes_csv()

