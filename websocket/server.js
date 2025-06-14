const WebSocket = require('ws');
const redis = require('redis');

const wss = new WebSocket.Server({ port: 8080 });
const redisClient = redis.createClient({ host: 'redis', port: 6379 });

console.log("WebSocket server started on ws://localhost:8080");

wss.on('connection', (ws) => {
    console.log("New client connected");

    const streamLogs = async () => {
        redisClient.keys("log:*", (err, keys) => {
            if (err) return console.error("Redis error:", err);

            keys.sort().reverse().slice(0, 10).forEach((key) => {
                redisClient.get(key, (err, value) => {
                    if (err) return;
                    ws.send(value);
                });
            });
        });
    };

    streamLogs();
    const interval = setInterval(streamLogs, 5000); // push every 5s

    ws.on('close', () => {
        clearInterval(interval);
        console.log("Client disconnected");
    });
});