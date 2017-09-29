FROM node:7

# set up angular cli
RUN yarn global add @angular/cli@1.2.7

WORKDIR /app
COPY package.json /app
COPY yarn.lock /app
RUN yarn install --pure-lockfile
COPY . /app

# create dist
RUN ng build --prod
