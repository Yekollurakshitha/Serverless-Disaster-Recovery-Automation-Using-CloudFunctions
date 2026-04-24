import boto3
import json
import time

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

BUCKET_NAME = "dr-backup-bucket"
BACKUP_FILE = "backup.zip"

def lambda_handler(event, context):
    print("🚨 Disaster detected! Starting recovery process...")

    try:
        # Step 1: Fetch backup from S3
        print(f"Fetching backup from bucket: {BUCKET_NAME}")
        s3.download_file(BUCKET_NAME, BACKUP_FILE, f"/tmp/{BACKUP_FILE}")

        # Step 2: Launch new EC2 instance
        print("Launching new EC2 instance...")
        response = ec2.run_instances(
            ImageId='ami-12345678',  # Replace with valid AMI
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            KeyName='your-key-pair'  # Replace with your key
        )

        instance_id = response['Instances'][0]['InstanceId']
        print(f"✅ Instance created: {instance_id}")

        # Step 3: Wait for instance to initialize
        print("Waiting for instance to be ready...")
        time.sleep(30)

        # Step 4: (Optional) Restore backup (custom logic)
        print("Restoring backup (implement your logic here)")

        # Step 5: Tag instance
        ec2.create_tags(
            Resources=[instance_id],
            Tags=[{'Key': 'Name', 'Value': 'DR-Recovery-Instance'}]
        )

        print("🎉 Recovery completed successfully!")

        return {
            'statusCode': 200,
            'body': json.dumps('Recovery completed successfully')
        }

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Recovery failed')
        }
