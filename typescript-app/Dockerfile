#base image
FROM node:lts-alpine
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json
COPY tsconfig.json /app/tsconfig.json
COPY src /app/src
COPY public /app/public
COPY babel.config.js /app/babel.config.js
RUN npm install
RUN npm install @vue/cli@3.7.0 -g
CMD ["npm", "run", "serve"]