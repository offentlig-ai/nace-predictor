# A simple test client

## Install and run locally

You have to put the url to the api in a variable in your .env file:

```
echo "REACT_APP_API_URL=http://localhost:8081" > .env
```

Then

```
npm install
npm start
```

Point you browser to <http://localhost:3000/>

## Docker

To build and run the test client in a Docker container:

```
docker build -t offentlig-ai/nace-predictor-test-client:latest .
docker run -p 8080:3000 -e REACT_APP_API_URL=http://localhost:8081 -d offentlig-ai/nace-predictor-test-client:latest
```
