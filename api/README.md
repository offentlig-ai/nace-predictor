# The API

## Requirements

As the api uses fastText you will need to install requirements as pr <https://github.com/facebookresearch/fastText/tree/master/python#requirements>

```
sudo apt-get install python3-pybind11
```

## Install and run locally

```
pip3 install --user --no-cache-dir -r requirements.txt
python3 -m app
```

## Docker

To build and run the api in a Docker container:

```
docker build -t offentlig-ai/nace-predictor-api:latest .
docker run -p 8081:8081 -d offentlig-ai/nace-predictor-api:latest
```
