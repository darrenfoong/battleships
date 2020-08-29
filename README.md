# Battleships (on Amazon Web Services)

A very simple game to learn how to use serverless technology on Amazon
Web Services.

# Prerequisites

- Python 3
- IAM user with administrator permissions ([link](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-linux.html))
- Docker
- AWS SAM CLI
  - Run `pip install --user aws-sam-cli`.
  - `sam` is in `~/.local/bin`. You can find the actual folder with
    `python -m site --user-base`.
  - On Linux: don't use [Homebrew](https://github.com/aws/aws-sam-cli/issues/1424).

# Running locally

- Run `sam local start-api`.
- Run `docker run -d --name dynamodb amazon/dynamodb-local`
- Run `docker run --rm -it -e AWS_ACCESS_KEY_ID=a -e AWS_SECRET_ACCESS_KEY=b -e AWS_DEFAULT_REGION=ap-southeast-1 amazon/aws-cli dynamodb list-tables --endpoint-url http://172.17.0.2:8000`

# Deploying

- Run `sam build`.
- Run `sam deploy --guided` or `sam deploy` if you already have a
  `samconfig.toml` file.

# Architecture

- Front-end: React single-page application hosted on Amazon S3.
  - Possible: Use AWS Amplify Console
- Gateway: Amazon API Gateway.
- Back-end: Python functions hosted on AWS Lambda.
- Persistence: Amazon DynamoDB.
- Security: Amazon Cognito.

# API

A very simple game has a very simple API.

```
- Create a game: POST /game
- Get all games: GET /game
- Get game as player: GET /game/{id}/{player_id}
- Perform action in game: POST /game/{id}/{player_id}
```
