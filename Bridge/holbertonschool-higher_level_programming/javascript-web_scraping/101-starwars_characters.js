#!/usr/bin/node

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Constructing the API URL for the specific film using the film ID (provided as command-line argument)
const apiURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

// Function that returns a promise to fetch a character's data by URL
const getCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    // Sending a GET request to fetch the character data
    request(url, (err, res, bd) => {
      // If there is an error, the promise is rejected
      if (err) {
        reject(err);
      } else {
        // Parsing the response body to extract the character's name
        const charName = JSON.parse(bd).name;
        // Resolving the promise with the character's name
        resolve(charName);
      }
    });
  });
};

// Main function that fetches the characters and logs their names in order
const fetchCharacters = async () => {
  try {
    // Fetching the film's data and getting the list of character URLs
    const response = await new Promise((resolve, reject) => {
      request(apiURL, (error, response, body) => {
        // If an error occurs, reject the promise
        if (error) {
          reject(error);
        } else {
          // Resolving the promise with the 'characters' array from the film data
          resolve(JSON.parse(body).characters);
        }
      });
    });

    // Looping through each character URL and fetching their name
    for (const characterURL of response) {
      // Using the 'getCharacterName' function to fetch and log each character's name
      const charName = await getCharacterName(characterURL);
      console.log(charName);
    }
  } catch (error) {
    // Logging any error that occurs during the process
    console.error(error);
  }
};

// Calling the main function to start the process
fetchCharacters();
