# The API

## To work in a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

## Install and run locally

```
pip install --no-cache-dir -r requirements.txt
python3 -m app
# In another terminal:
curl -H "Accept: application/json" "http://localhost:8081/api?q=lakseoppdrett"
```

## Docker

To build and run the api in a Docker container:

```
docker build -t offentlig-ai/nace-predictor-api:latest .
docker run -p 8081:8081 -d offentlig-ai/nace-predictor-api:latest
```
