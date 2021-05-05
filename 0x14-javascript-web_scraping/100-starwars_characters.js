#!/usr/bin/node
// Print characters name

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/';
request(url, function (error, response, body) {
  if (error) {
    console.error(error); // Print the error if one occurred
  } else {
    for (const person of JSON.parse(body).results) {
      for (const film of person.films) {
        if (film.split('/')[5] === process.argv[2]) {
          console.log(person.name);
          break;
        }
      }
    }
  }
});
