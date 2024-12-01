#!/usr/bin/node

// Importing the 'fs' (file system) module from Node.js to handle file operations
const fs = require('node:fs');

// Reading the content of the file provided as a command-line argument
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  // If an error occurs during file reading, it will be logged to the console
  if (err) {
    console.error(err);
    return; // Exit the function if there is an error
  }

  // If the file is read successfully, its content is logged to the console
  console.log(data);
});
