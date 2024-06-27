from typing import NoReturn
from decimal import Decimal

import argparse
import boto3
import json

def insert(table_name: str, file_path: str) -> NoReturn:

    print(f"criando cliente DynamoDB")
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table(table_name)

    print(f"abrindo arquivo '{file_path}'")
    with open(file_path, 'r', encoding='utf-8') as file:

        json_list = json.load(file, parse_float=Decimal)

        with table.batch_writer() as batch:

            print(f"inserindo itens na tabela '{table_name}': ", end="")
            for json_item in json_list:
                print(".", end="")
                batch.put_item(Item=json_item)

        print(f"\n{len(json_list)} itens inseridos com sucesso!")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--table', required=True)
    parser.add_argument('-f', '--file', required=True)
    args = parser.parse_args()

    table_name = args.table
    file_path = args.file

    insert(table_name, file_path)