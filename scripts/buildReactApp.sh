#!/bin/bash
set -e

reactAppDir=app/static

cd ${reactAppDir}
npm install
npm run build
cd ${HOME}