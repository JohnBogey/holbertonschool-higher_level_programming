#!/usr/bin/node
// prints status code

const request = require('request');

request(process.argv[2], function (error, response) {
  console.log('code:', response && response.statusCode);
});
