from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', endpoint_url = 'http://localhost:4000')

table = dynamodb.Table('Movies')

with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        year  = int(movie['year'])
        title = movie['title']
        info  = movie['title']

        print("Adding movie: ", year, title.encode('ascii', 'ignore'))

        table.put_item(
            Item = {
                'year': year,
                'title': title,
                'info': info,
            }
        )