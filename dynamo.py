import boto3
import json
import sys
from decimal import Decimal

def batch_load_dynamo(table_name, path):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table(table_name)
    json_list = list()
    
    with open(path, 'r', encoding='utf-8') as file:
        print(f'Abrindo arquivo {file}')
        json_list = json.load(file, parse_float=Decimal)
    
        print(f'Inserindo dados na tabela {table}')
        with table.batch_writer() as batch:
            for json_item in json_list:
                batch.put_item(Item=json_item)
            
if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(1)
    path = sys.argv[1]
    table_name = sys.argv[2]

    batch_load_dynamo(table_name, path)