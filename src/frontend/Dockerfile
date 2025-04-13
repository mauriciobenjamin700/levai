FROM node:23-alpine3.21

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "-run", "start"]