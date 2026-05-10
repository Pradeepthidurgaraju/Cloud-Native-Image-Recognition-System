import json
import boto3

def lambda_handler(event, context):
    # This triggers when a new image is uploaded to S3
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(f"New image detected: {key} in bucket {bucket}. Triggering Recognition API...")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Trigger successful')
    }
