from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', endpoint_url = 'http://localhost:4000')

table = dynamodb.Table('Movies')

title = 'The Big New Movie'
year = 2015

response = table.update_item(
    Key = {
        'year': year,
        'title': title
    },
    UpdateExpression = 'set info.rating = :r, info.plot = :p, info.actors = :a',
    ExpressionAttributeValues = {
        ':r': decimal.Decimal(5.5),
        ':p': 'Everything happens all at once',
        ':a': ['Larry', 'Moe', 'Curly']
    },
    ReturnValues = 'UPDATED_NEW'
)

print('PutItem succeeded:')
print(json.dumps(response, indent = 4, cls = DecimalEncoder))