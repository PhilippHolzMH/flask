import boto3

s3client=boto3.client("s3")

def list_and_count(bucketname):
    my_bucket = s3client.list_objects(Bucket=bucketname)['Contents']
    result = []
    for objects in my_bucket:
        filename = objects['Key']
        content = str(s3client.get_object(Bucket=bucketname, Key=filename)['Body'].read())
        wordlist = content.split(" ")
        wordcount = len(wordlist)
        dict = {
            "key" : filename,
            "words" : wordcount
        }
        result.append(dict)
    return result