FROM python:3

RUN git clone https://github.com/facebookresearch/fastText.git /tmp/fastText  && \
  cd /tmp/fastText && \
  pip install . && \
  rm -rf /tmp/fastText && \
  cd /

COPY ./app /app
COPY ./dockerEntryPoint.sh /

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/bash", "/dockerEntryPoint.sh"]