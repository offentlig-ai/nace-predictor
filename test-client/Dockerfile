FROM node:8-alpine

# Create app directory
RUN mkdir -p /usr/src/app && chmod 777 /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/package.json
COPY package-lock.json /usr/src/app/package-lock.json

# Install app dependencies
RUN npm install --only=production --loglevel=warn

COPY public /usr/src/app/public

# most volatile directory latest, in order to reuse layers.
COPY src /usr/src/app/src

RUN npm run build

EXPOSE 3111

CMD [ "npm", "start" ]
