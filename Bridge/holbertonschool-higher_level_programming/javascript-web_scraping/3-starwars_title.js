#!/usr/bin/node

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Constructing the URL for the API request by appending the film ID (from the command line argument)
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

// Making the GET request to the constructed URL
request(url, (error, response, body) => {
  // If there is an error, it will be logged; otherwise, the title of the film is logged
  console.log(error || JSON.parse(body).title);
});
