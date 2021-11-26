import boto3
import json
from datetime import datetime

topic_ARN = 'arn:aws:sns:us-east-2:425676887181:testing'
sns_client = boto3.client(
    'sns',
    aws_access_key_id='AKIAWGHCR2SGQCR72S4B',
    aws_secret_access_key='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',
    region_name='us-east-2'
)

for i in range(2):
    publish_data = {
        "id": str(i),
        "pod0": 80, 
        "pod1": 57, 
        "pod2": 35, 
        "pod3": 29, 
        "pod4": 0, 
        "pod5": -15, 
        "pod6": -27, 
        "pod7": 26, 
        "gyroscope_x": 500, 
        "gyroscope_y": 412, 
        "gyroscope_z": -99, 
        "accelerometer_x": -2, 
        "accelerometer_y": 2, 
        "accelerometer_z": 4, 
        "magnetometer_x": -1,
        "magnetometer_y": 0, 
        "magnetometer_z": "-0.3", 
        "magnetometer_w": "0.7"
    }

    response = sns_client.publish(
        TopicArn=topic_ARN,
        Message=json.dumps(publish_data),
        Subject='testing',
    )

    print(response['ResponseMetadata']['HTTPStatusCode'])


class SenderSNS():
    def __init__(self, key_id, secret, region_name, topic_ARN):
        self.sns_client = boto3.client(
            'sns',
            aws_access_key_id=key_id,
            aws_secret_access_key=secret,
            region_name=region_name,
        )
        self.topic_ARN = topic_ARN

    def send_data(self, publish_data):
        publish_data['ts'] = datetime.now()
        response = sns_client.publish(
            TopicArn=self.topic_ARN,
            Message=json.dumps(publish_data),
            Subject='testing',
        )
        return response
