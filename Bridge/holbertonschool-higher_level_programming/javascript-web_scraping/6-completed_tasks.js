#!/usr/bin/node

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Getting the API URL from the command-line argument
const apiUrl = process.argv[2];

// Initializing an empty object to store the count of completed tasks for each user
const userCompletedTasks = {};

// Making an HTTP GET request to the API URL
request(apiUrl, { json: true }, (error, response, body) => {
  // If no error occurs, process the response body
  if (!error) {
    // Looping through each task in the response body
    body.forEach((task) => {
      // Check if the task is marked as completed
      if (task.completed) {
        const userId = task.userId; // Get the userId for the task
        // Increment the completed task count for the user
        userCompletedTasks[userId] = (userCompletedTasks[userId] || 0) + 1;
      }
    });
    // Log the final count of completed tasks for each user
    console.log(userCompletedTasks);
  }
});
