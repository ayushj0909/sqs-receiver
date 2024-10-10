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
region_name = 'ap-south-1'

sqs_client = boto3.client(
    'sqs',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name,
)

while True:
    try:
        response = sqs_client.receive_message(
            QueueUrl=sqs_queue_url,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=10,
        )

        messages = response.get('Messages', [])
        if not messages:
            logger.info("No messages to process.")
            continue  # Skip the rest of the loop if there are no messages

        for message in messages:
            # Parse the message body as JSON
            try:
                message_body = json.loads(message['Body'])
                logger.info(f"Received message: {message_body}")

                # Process your message as needed
                # Example: accessing specific fields
                account_id = message_body.get('account_id')
                trigger_id = message_body.get('trigger_id')
                org_name = message_body.get('org_name')

                logger.info(f"Account ID: {account_id}, Trigger ID: {trigger_id}, Org Name: {org_name}")

            except json.JSONDecodeError:
                logger.error("Failed to decode JSON from message body.")
                continue

            # Delete the message from the queue after processing
            sqs_client.delete_message(
                QueueUrl=sqs_queue_url,
                ReceiptHandle=message['ReceiptHandle'],
            )
            logger.info("Deleted message from queue.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

    time.sleep(sleep_time)
