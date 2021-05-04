#!/usr/bin/node
// prints status code

const request = require('request');

request(process.argv[2], function (error, response) {
  if (error) {
    console.error(error); // Print the error if one occurred
  }
  console.log('code:', response && response.statusCode);
});
