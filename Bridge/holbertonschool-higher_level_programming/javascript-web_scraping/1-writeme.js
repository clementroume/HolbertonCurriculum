#!/usr/bin/node

// Importing the 'fs' (file system) module from Node.js to handle file operations
const fs = require('node:fs');

// Writing data to a file specified as a command-line argument
fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err, data) => {
  // If an error occurs during the file writing process, it will be logged to the console
  if (err) {
    console.error(err);
  }
});
