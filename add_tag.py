import boto3

tagkey=input('Please enter tag Key:  ')
tagval=input('Please enter tag Value:  ')

session = boto3.Session(profile_name='abc_user',region_name='us-east-1')
rds_client = session.client('rds')
#db_instance_info = rds_client.describe_db_instances(DBInstanceIdentifier='**myinstancename**')
#db_instance_info = rds_client.describe_db_clusters(DBClusterIdentifier='sitvodka')
db_instance_info = rds_client.describe_db_clusters()
print('\nAdded tags for Below servers.\n TagKey: ',tagkey,' TagValue: ',tagval,'\n')
for each_db in db_instance_info['DBClusters']:
	response = rds_client.add_tags_to_resource(ResourceName=each_db['DBClusterArn'],Tags=[{'Key': tagkey,'Value': tagval},])
	print(each_db['DBClusterIdentifier'])