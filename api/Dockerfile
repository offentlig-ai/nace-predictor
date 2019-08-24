FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip3 install pybind11

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8081

ENTRYPOINT ["python3"]

CMD ["-m", "app"]
