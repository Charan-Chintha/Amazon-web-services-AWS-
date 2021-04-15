import boto3

tagkey=input('Please enter tag Key:  ')
tagval=input('Please enter tag Value:  ')

session = boto3.Session(profile_name='abc_user',region_name='us-east-1')
rds_client = session.client('rds')
#db_instance_info = rds_client.describe_db_clusters(DBClusterIdentifier='my_server')
db_instance_info = rds_client.describe_db_clusters()
print('\nServers List having TagKey: ',tagkey,' TagValue: ',tagval,'\n')
for each_db in db_instance_info['DBClusters']:
	response = rds_client.list_tags_for_resource(ResourceName=each_db['DBClusterArn'])['TagList']
	for tag in response:
		if (tag['Key'] == tagkey and tag['Value'] == tagval):
			#print(response)
			print(each_db['DBClusterIdentifier'])