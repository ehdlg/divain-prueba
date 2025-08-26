FROM node:20-alpine

WORKDIR /app

COPY frontend/package*.json ./
RUN npm install

COPY frontend .

EXPOSE 5173

ENV HOST=0.0.0.0

CMD ["npm", "run", "dev"]
