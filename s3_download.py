#! /usr/bin/python
import boto3
session = boto3.Session(profile_name='abc_user')
#print(session.available_profiles)
client = session.client('s3')
filename=input('Please enter the filename: ')
bucket_name='hrc-db-dumps'
download = client.download_file(bucket_name,filename,filename)
print('Download successfully')
