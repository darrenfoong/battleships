import boto3
import json
import jsonpickle
import os

from common import GameDto, decode_perform_action_request

if os.getenv("AWS_SAM_LOCAL", ""):
    client = boto3.client("dynamodb", endpoint_url="http://172.17.0.2:8000")
    BATTLESHIPS_TABLE = "battleships-table"
else:
    client = boto3.client("dynamodb")
    BATTLESHIPS_TABLE = os.environ["TABLE_NAME"]


def lambda_handler(event, context):
    perform_action_request = json.loads(
        event["body"], object_hook=decode_perform_action_request
    )

    id = event["pathParameters"]["id"]
    player = event["pathParameters"]["player"]

    game = jsonpickle.decode(
        GameDto(
            client.get_item(
                TableName=BATTLESHIPS_TABLE,
                Key={"id": {"S": str(id)}},
                ConsistentRead=True,
            )["Item"]
        ).value
    )

    game.perform_action(
        player,
        perform_action_request.x,
        perform_action_request.y,
        perform_action_request.weapon,
    )

    client.update_item(
        TableName=BATTLESHIPS_TABLE,
        Key={"id": {"S": str(id)}},
        UpdateExpression="SET #value = :value",
        ExpressionAttributeNames={"#value": "value"},
        ExpressionAttributeValues={":value": {"S": jsonpickle.encode(game)}},
    )

    return {"statusCode": 200}
