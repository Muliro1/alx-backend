import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const client = createClient();
const HOST = '127.0.0.1';
const PORT = 1245;
const listProducts = [{
  id: 1, name: 'Suitcase 250', price: 50, stock: 4,
},
{
  id: 2, name: 'Suitcase 450', price: 100, stock: 10,
},
{
  id: 3, name: 'Suitcase 650', price: 350, stock: 2,
},
{
  id: 4, name: 'Suitcase 1050', price: 550, stock: 5,
},
];

/**
 * Returns the product object from the listProducts array that matches the given id.
 *
 * @param {number} id - The id of the product to search for.
 * @returns {object | undefined} - The product object if found, otherwise undefined.
 */
function getItemById(id) {
  /**
   * Iterates over the listProducts array and returns the product object that has the given id.
   *
   * @param {object} product - The product object to check.
   * @returns {object | undefined} - The product object if it has the given id, otherwise undefined.
   */
  return listProducts.find((product) => product.id === id);
}

// Redis client ops
client.on('error', (error) => {
  console.log(`Redis client not connected to server ${error.message}`);
});

/**
 * Stores itemId-stock key-value pair in redis
 * @param {string} itemId - item id
 * @param {number} stock - product stock
 */
function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}


/**
 * Asynchronously retrieves the current stock value associated with a given item ID.
 *
 * @param {string} itemId - The ID of the item to retrieve the stock value for.
 * @return {Promise<string | null>} A promise that resolves to the current stock value
 * as a string, or null if the item does not exist in Redis.
 */
async function getCurrentReservedStockById(itemId) {
  // Use the promisify utility function to convert the client's get method to a promise-based
  // function that can be awaited.
  const getAsync = promisify(client.get).bind(client);

  // Retrieve the value associated with the item ID from Redis.
  const value = await getAsync(`item.${itemId}`);

  // Return the retrieved value, which may be null if the item does not exist in Redis.
  return value;
}

// Express app routes
/* Get list of all products */
app.get('/list_products', (_req, res) => {
  res.send(listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  })));
});

/* Get items by given id */
app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(Number(itemId));
  if (product === undefined) {
    res.statusCode = 404;
    res.send({ status: 'Product not found' });
  } else {
    const reserveStock = await getCurrentReservedStockById(product.id);
    res.send({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
      currentQuantity: reserveStock === null ? product.stock : Number(reserveStock),
    });
  }
});

/* Reserve a product with given id if it exists and in stock */
app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(Number(itemId));
  if (product === undefined) {
    res.statusCode = 404;
    res.send({ status: 'Product not found' });
    return;
  }
  let reserveStock = await getCurrentReservedStockById(product.id);
  reserveStock = reserveStock === null ? product.stock : Number(reserveStock);
  if (!reserveStock) {
    res.send({ status: 'Not enough stock available', ItemId: product.id });
  } else {
    reserveStockById(product.id, reserveStock - 1);
    res.send({ status: 'Reservation confirmed', ItemId: product.id });
  }
});

app.listen(PORT, HOST, () => {
  console.log(`Server is live at ${HOST}:${PORT}`);
});
