import { print, createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});
redisClient.on('connect', () => console.log('Redis client connected to the server'));

console.log(redisClient.connected);
/**
 * Set a key-value pair in redis
 * @param {string} schoolName - key
 * @param {string} value      - value
 */
function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}

/**
 * This function retrieves the value associated with a given key from the Redis store
 * and logs it to the console if it exists.
 *
 * @param {string} schoolName - The key to search for in the Redis store.
 * @return {void} This function does not return anything.
 */
function displaySchoolValue(schoolName) {
  // Get the value associated with the given key from the Redis store
  redisClient.get(schoolName, (_error, value) => {
    // If the value exists, log it to the console
    if (value) console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
