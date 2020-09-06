import boto3
import json
import jsonpickle
import uuid
import os

from common import GameDto

if os.getenv("AWS_SAM_LOCAL", ""):
    client = boto3.client("dynamodb",
                          endpoint_url="http://172.17.0.2:8000")
    BATTLESHIPS_TABLE = "battleships-table"
else:
    client = boto3.client("dynamodb")
    BATTLESHIPS_TABLE = os.environ["TABLE_NAME"]


def lambda_handler(event, context):
    games_dto = list(map(lambda item: GameDto(item), client.scan(
        TableName=BATTLESHIPS_TABLE
    )["Items"]))

    return {
        "statusCode": 200,
        "body": json.dumps(games_dto.to_json()),
    }
