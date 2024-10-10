import boto3
import os
import time
import logging
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
sqs_queue_url = os.environ['SQS_QUEUE_URL']
sleep_time = int(os.environ['SLEEP_TIME'])
region_name = 'ap-south-1'  # Change to your region

sqs_client = boto3.client(
    'sqs',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name,
)

# Initial trigger_id digit
trigger_id_digit = 0  # Start from 0

while True:
    try:
        # Create the JSON payload
        payload = {
            "account_id": "dummy_id",
            "trigger_id": f"{trigger_id_digit}c93c629-c6ba-4392-a8f9-04e602432cbd",  # Incrementing the first digit
            "org_name": "amnic"
        }

        # Convert the payload to JSON string
        message_body = json.dumps(payload)

        response = sqs_client.send_message(
            QueueUrl=sqs_queue_url,
            MessageBody=message_body,
        )

        logger.info(f"Sent message: {message_body} (Message ID: {response['MessageId']})")

        # Increment the first digit of the trigger_id
        trigger_id_digit += 1

    except Exception as e:
        logger.error(f"An error occurred while sending message: {e}")

    time.sleep(sleep_time)
