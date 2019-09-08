# The API

## Install and run locally

```
pip3 install --user --no-cache-dir -r requirements.txt
python3 -m app
# In another terminal:
curl -H "Accep: application/json" "http://localahost:8081/api?q=lakseoppdrett"
```

## Docker

To build and run the api in a Docker container:

```
docker build -t offentlig-ai/nace-predictor-api:latest .
docker run -p 8081:8081 -d offentlig-ai/nace-predictor-api:latest
```
