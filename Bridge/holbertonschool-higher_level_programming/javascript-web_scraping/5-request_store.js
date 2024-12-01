#!/usr/bin/node

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Importing the 'fs' (file system) module from Node.js to handle file operations
const fs = require('node:fs');

// Getting the API URL from the command-line argument
const apiUrl = process.argv[2];

// Making an HTTP GET request to the API URL
request(apiUrl, (error, response, body) => {
  // If no error occurs, proceed with writing the data to a file
  if (!error) {
    const lorem = body; // Storing the API response body (data) in the 'lorem' variable

    // Writing the fetched data to a file specified by the third command-line argument
    fs.writeFile(process.argv[3], lorem, 'utf8', (err, data) => {
      // If an error occurs during the file writing process, log the error to the console
      if (err) {
        console.error(err);
      }
    });
  }
});
