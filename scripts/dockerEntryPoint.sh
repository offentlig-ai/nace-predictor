#!/bin/bash
set -e

gsutil cp gs://ai-lab-modeller/nace_model.bin /app/static/model.bin

python /app/app.py