import boto3
import json

s3client=boto3.client("s3")

def list_and_count(bucketname):
    my_bucket = s3client.list_objects(Bucket=bucketname)['Contents']
    for objects in my_bucket:
        filename = objects['Key']
        print(filename)
        content = str(s3client.get_object(Bucket=bucketname, Key=filename)['Body'].read())
        wordlist = content.split(" ")
        wordcount = len(wordlist)
        print(wordcount)