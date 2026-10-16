#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const todos = JSON.parse(body);
  const completed = {};

  todos.forEach((task) => {
    if (task.completed) {
      if (completed[task.userId]) {
        completed[task.userId] += 1;
      } else {
        completed[task.userId] = 1;
      }
    }
  });

  console.log(completed);
});
