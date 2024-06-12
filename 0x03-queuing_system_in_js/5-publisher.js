import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

/**
 * Publishes a message to the 'holberton school channel' in Redis after a specified delay.
 *
 * @param {string} message - The message to be published.
 * @param {number} time - The delay in milliseconds before publishing the message.
 */
function publishMessage(message, time) {
  // Wrap the publish operation in a setTimeout to introduce a delay
  setTimeout(() => {
    // Log a message indicating that the message is about to be sent
    console.log(`About to send ${message}`);
    
    // Publish the message to the 'holberton school channel' in Redis
    redisClient.publish('holberton school channel', message);
  }, time);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
