import boto3
import json

topic_ARN = 'arn:aws:sns:us-east-2:425676887181:testing'
sns_client = boto3.client(
    'sns',
    aws_access_key_id = 'AKIAWGHCR2SGQCR72S4B',
    aws_secret_access_key = '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',
    region_name = 'us-east-2'
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
        "orientation_x": -1,
        "orientation_y": 0, 
        "orientation_z": "-0.3", 
        "orientation_w": "0.7"
    }

    response = sns_client.publish(
        TopicArn = topic_ARN,
        Message = json.dumps(publish_data),
        Subject = 'testing',
    )

    print(response['ResponseMetadata']['HTTPStatusCode'])