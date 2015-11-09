from __future__ import print_function # Python 2/3 compatibility
import boto3

# dynamodb = boto3.resource('dynamodb')
dynamodb = boto3.resource('dynamodb', endpoint_url = 'http://localhost:4000')

table = dynamodb.create_table(
    TableName = 'Movies',
    KeySchema = [
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status: ", table.table_status)