FROM python:3

RUN git clone https://github.com/facebookresearch/fastText.git /tmp/fastText  && \
  cd /tmp/fastText && \
  pip install . && \
  rm -rf /tmp/fastText && \
  cd /

COPY ./app /app

WORKDIR /app

ADD https://storage.googleapis.com/ai-lab-modeller/nace_model.bin /app/static/model.bin

RUN pip install -r requirements.txt

CMD ["python", "app.py"]