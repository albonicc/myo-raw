import boto3
import json
from datetime import datetime

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
        ts = datetime.timestamp(datetime.now())

        publish_data['ts'] = str(ts)
        print(publish_data)
        response = self.sns_client.publish(
            TopicArn=self.topic_ARN,
            Message=json.dumps(publish_data),
            Subject='testing',
        )
        return response
