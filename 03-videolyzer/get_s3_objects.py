# coding: utf-8
import boto3

s3_client = boto3.client('s3')

def get_objects(bucket):
    """ Get a list of keys in an S3 bucket."""
    keys = []
    resp = s3_client.list_objects_v2(Bucket=bucket)
    for obj in resp['Contents']:
        keys.append(obj['Key'])
    return keys
    
    
get_objects('keithvideolyzervideos123456')
