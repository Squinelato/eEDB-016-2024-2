from typing import NoReturn
from decimal import Decimal
from more_itertools import batched

import argparse
import boto3
import json

def insert(table_name: str, file_path: str) -> NoReturn:
    """
    Insert a list of JSON items into a DynamoDB table using the batch
    write operator in chunks of 25 items each.

    Keyword arguments:
    table_name -- The name of the DynamoDB table
    file_path -- the path to the file containing a JSON list of items
    """
    print(f"Creating DynamoDB client")
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table(table_name)

    print(f"Opening file '{file_path}'")
    with open(file_path, 'r', encoding='utf-8') as file:

        json_list = json.load(file, parse_float=Decimal)

        batches = batched(json_list, 25)
        print("Splitting items into batches of 25 items")

        for index, batch in enumerate(batches):

            print(f"Inserting {index+1}º batch with {len(batch)} items")

            with table.batch_writer() as batch_writer:

                print(f"Inserting items into '{table_name}' table: ", end="")
                for item in batch:
                    print(".", end="")
                    batch_writer.put_item(Item=item)

        print(f"\nItems inserted successfully!")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--table', required=True)
    parser.add_argument('-f', '--file', required=True)
    args = parser.parse_args()

    table_name = args.table
    file_path = args.file

    insert(table_name, file_path)