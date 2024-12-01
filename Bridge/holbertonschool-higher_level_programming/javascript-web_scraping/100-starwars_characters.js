#!/usr/bin/node

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Constructing the API URL by appending the film ID (from the command line argument) to the base URL
const apiURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

// Making the GET request to fetch the film's data
request(apiURL, (error, response, body) => {
  // Parsing the response body to get the 'characters' array from the film's data
  const characters = JSON.parse(body).characters;

  // Looping through the list of character URLs associated with the film
  characters.forEach((character) => {
    // The character URL for each character is stored in 'charURL'
    const charURL = character;

    // Making a GET request to fetch the details of each character
    request(charURL, (err, res, bd) => {
      // Parsing the character data to extract the character's name
      const charName = JSON.parse(bd).name;

      // Logging the error (if any) or the character's name
      console.log(err || error || charName);
    });
  });
});
