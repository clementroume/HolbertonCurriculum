#!/usr/bin/node

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Getting the API URL from the command-line argument
const apiUrl = process.argv[2];

// Setting the ID for the character "Wedge Antilles" (a pilot in the Star Wars universe)
const wedgeId = '18';

// Making an HTTP GET request to the API URL
request(apiUrl, (error, response, body) => {
  // Parsing the response body (assumed to be in JSON format) and getting the 'results' array
  const results = JSON.parse(body).results;

  // Initialize a counter to track how many films Wedge Antilles appears in
  let count = 0;

  // Loop through each film in the 'results' array
  results.forEach((film) => {
    // Getting the 'characters' array for each film
    const characters = film.characters;

    // Checking if the character Wedge Antilles (ID 18) is listed in the film's character URLs
    if (characters.some((url) => url.includes(`/people/${wedgeId}`))) {
      count++; // Increment the count if Wedge appears in this film
    }
  });

  // Log either the error (if it occurred) or the total count of films featuring Wedge Antilles
  console.log(error || count);
});
