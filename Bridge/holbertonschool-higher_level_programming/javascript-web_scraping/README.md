# JavaScript Web Scraping - Holberton School

Welcome to the **JavaScript Web Scraping** project repository! This project is part of the **Holberton School Higher-Level Programming** curriculum and focuses on web scraping techniques using JavaScript and Node.js. It explores how to interact with web APIs and retrieve data for various applications. Each task builds upon the previous one, helping you understand different HTTP requests and how to handle asynchronous operations with callbacks, promises, and async/await.

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project focuses on fetching data from various APIs using JavaScript and Node.js. It demonstrates how to handle asynchronous operations and process data in real-time by making HTTP requests. Key concepts covered include:

- Sending GET requests to fetch data from APIs.
- Handling asynchronous operations using callbacks, promises, and async/await.
- Parsing and manipulating JSON data.
- Using HTTP status codes to handle request responses.
- Storing and processing data from external sources like the Star Wars API.

The repository includes several tasks that gradually build your understanding of web scraping with Node.js, focusing on tasks such as fetching film data from the Star Wars API, listing characters, and more.

---

## Project Structure

Here’s an overview of the files included in the `javascript-web-scraping` directory:

| File                         | Description                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------- |
| `0-readme.js`                | Reads the content of a file and displays it on the console.                                             |
| `1-writeme.js`               | Writes a string to a file, creating it if it doesn't exist.                                             |
| `2-statuscode.js`            | Fetches the status code of a given URL using a GET request and logs the HTTP status code.               |
| `3-starwars_title.js`        | Fetches the title of a Star Wars film based on the film ID passed via the command line.                 |
| `4-starwars-count.js`        | Counts how many times the character "Wedge Antilles" appears in the films of the Star Wars API.         |
| `5-request_store.js`         | Saves the HTML content from a specified URL to a file.                                                  |
| `6-completed_tasks.js`       | Parses a list of tasks from a JSON placeholder API and counts how many tasks each user has completed.   |
| `100-starwars_characters.js` | Retrieves and logs the names of characters in a specific Star Wars film in the correct order.           |
| `101-starwars_characters.js` | Retrieves and logs the names of characters in a specific Star Wars film using async/await for ordering. |

---

## Learning Objectives

- Understand how to make HTTP requests in JavaScript using Node.js and the `request` module.
- Learn how to process JSON data returned from API responses.
- Gain experience working with asynchronous code using callbacks, promises, and async/await.
- Handle HTTP response codes and errors in API requests.
- Develop the skills to scrape and process data from external sources such as public APIs.
- Learn how to manipulate and store data in a structured format (JSON, files, etc.).

---
