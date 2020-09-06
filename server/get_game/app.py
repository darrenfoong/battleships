import boto3
import json
import jsonpickle
import uuid
import os

from common import GameDto

if os.getenv("AWS_SAM_LOCAL", ""):
    client = boto3.client("dynamodb", endpoint_url="http://172.17.0.2:8000")
    BATTLESHIPS_TABLE = "battleships-table"
else:
    client = boto3.client("dynamodb")
    BATTLESHIPS_TABLE = os.environ["TABLE_NAME"]


def lambda_handler(event, context):
    id = event["pathParameters"]["id"]
    player_id = event["pathParameters"]["player_id"]

    game_dto = GameDto(
        client.get_item(
            TableName=BATTLESHIPS_TABLE, Key={"id": {"S": str(id)}}, ConsistentRead=True
        )["Item"],
    )

    return {"statusCode": 200, "body": json.dumps(game_dto.to_json())}
