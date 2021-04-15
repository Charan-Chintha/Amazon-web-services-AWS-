#! /usr/bin/python
import boto3
session = boto3.Session(profile_name='abc_user')
#print(session.available_profiles)
client = session.client('s3')
filename=input('Please enter filepath:')
bucket_name='my_dumps'
upload = client.upload_file(filename,bucket_name,filename)
print('Upload successfully')
