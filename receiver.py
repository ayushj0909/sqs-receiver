import boto3
import os
import time

# Get AWS credentials and SQS queue URL from environment variables
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
sqs_queue_url = os.environ['SQS_QUEUE_URL']

# Specify your AWS region
region_name = 'ap-south-1'  # Change to your region

# Create an SQS client with the specified region
sqs_client = boto3.client(
    'sqs',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name,
)

while True:
    response = sqs_client.receive_message(
        QueueUrl=sqs_queue_url,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=10,
    )

    messages = response.get('Messages', [])
    for message in messages:
        print(f"Received message: {message['Body']}")

        # Delete the message after processing
        sqs_client.delete_message(
            QueueUrl=sqs_queue_url,
            ReceiptHandle=message['ReceiptHandle'],
        )

    time.sleep(5)
