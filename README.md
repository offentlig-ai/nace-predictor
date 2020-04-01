# Determine NACE-codes based on the description of the enterprise

This repository exposes an ML-model as a service that predicts NACE-codes based on various datasets. There is also a simple client GUI (React) you can use to play with the service.

An overview of the target solution architecture is [here](https://brreg.github.io/CA_NACE-predictor/) .

## The model

The model is developed over at <https://github.com/offentlig-ai/nace-notebooks> and is made available to the API.

## The API

[The API](./api) is implemented in Python (<http://flask.pocoo.org/>) and a specification will be made available. Currently the API is available at <http://35.228.204.120/api>. Example of usage:

```
curl -H "Accept: application/json" "http://35.228.204.120/api?q=Skogsdrift"
```

## A simple test client

We have made a simple [test client](./test-client) in React.

Screenshot: ![alt text](screenshot.png "Title")

For the time beeing the client is made avaialable here: [A simple test client](http://35.228.204.120/)

## Try it out with Docker locally

```
git clone https://github.com/offentlig-ai/nace-predictor.git
cd nace-predictor
docker build -t offentlig-ai/nace-predictor-api:latest ./api/.
docker build -t offentlig-ai/nace-predictor-test-client:latest ./test-client/.
docker-compose up
```

Then point your browser to <http://localhost:8080>

## Further work

Some further work based on this application has been done [here](https://github.com/datautvikling/nace-predictor).
