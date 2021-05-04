#!/usr/bin/node
// Print users with completed tasks

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error); // Print the error if one occurred
  } else {
    const users = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (!users[task.userId]) {
        users[task.userId] = 0;
      }
      if (task.completed === true) {
        users[task.userId] += 1;
      }
    }
    console.log(users);
  }
});
