import boto3

def receive_messages(queue_url):
    sqs = boto3.client('sqs', endpoint_url='http://localhost:4566', region_name='us-east-1')
    response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10)
    return response.get('Messages', [])