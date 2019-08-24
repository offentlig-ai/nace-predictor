# A simple test client

## Docker

To build and run the test client in a Docker container:

```
docker build -t offentlig-ai/nace-predictor-test-client:latest .
docker run -p 8080:3000 -e REACT_APP_API_URL=http://localhost:8081 -d offentlig-ai/nace-predictor-test-client:latest
```
