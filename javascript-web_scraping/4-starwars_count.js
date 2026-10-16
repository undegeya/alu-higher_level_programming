#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  let count = 0;

  data.results.forEach((movie) => {
    const found = movie.characters.some((character) => {
      return character.endsWith('/18/');
    });

    if (found) {
      count += 1;
    }
  });

  console.log(count);
});
