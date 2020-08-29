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
