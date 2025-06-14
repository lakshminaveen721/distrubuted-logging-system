FROM node:18
WORKDIR /app
COPY . .
RUN npm install ws redis
CMD ["node", "server.js"]