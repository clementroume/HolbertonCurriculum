#!/usr/bin/node

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Making an HTTP GET request to the URL passed as a command-line argument
request.get(process.argv[2]).on('response', (response) => {
  // Logging the status code of the HTTP response
  console.log(`code: ${response.statusCode}`);
});
