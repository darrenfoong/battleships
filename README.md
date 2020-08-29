# Battleships (on Amazon Web Services)

A very simple game to learn how to use serverless technology on Amazon
Web Services.

# Architecture

- Front-end: React single-page application hosted on Amazon S3.
  - Possible: Use AWS Amplify Console
- Gateway: Amazon API Gateway.
- Back-end: Python functions hosted on AWS Lambda.
- Persistence: Amazon DynamoDB.
- Security: Amazon Cognito? AWS IAM?

# API

A very simple game has a very simple API.

```
- Create a game: POST /game
- View all games: GET /game
- View game as player: GET /game/{id}/{player_id}
- Perform action in game: POST /game/{id}/{player_id}
```
