import boto3
import os
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
sqs_queue_url = os.environ['SQS_QUEUE_URL']

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

        for message in messages:
            logger.info(f"Received message: {message['Body']}")

            sqs_client.delete_message(
                QueueUrl=sqs_queue_url,
                ReceiptHandle=message['ReceiptHandle'],
            )
            logger.info("Deleted message from queue.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

    time.sleep(5)
