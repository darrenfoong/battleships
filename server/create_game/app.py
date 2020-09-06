import boto3
import json
import jsonpickle
import uuid
import os

from common import Game

if os.getenv("AWS_SAM_LOCAL", ""):
    client = boto3.client("dynamodb", endpoint_url="http://172.17.0.2:8000")
    BATTLESHIPS_TABLE = "battleships-table"
else:
    client = boto3.client("dynamodb")
    BATTLESHIPS_TABLE = os.environ["TABLE_NAME"]


def lambda_handler(event, context):
    create_game_request = json.loads(event["body"])

    id = uuid.uuid4()

    game = Game(create_game_request["width"], create_game_request["height"], 0)

    client.put_item(
        TableName=BATTLESHIPS_TABLE,
        Item={"id": {"S": str(id)}, "value": {"S": jsonpickle.encode(game)}},
    )

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "id": str(id),
            }
        ),
    }
