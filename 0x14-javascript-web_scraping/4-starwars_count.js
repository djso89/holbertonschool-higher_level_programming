#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let cnt = 0;
    const films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('/18/')) {
          cnt++;
          break;
        }
      }
    }
    console.log(cnt);
  }
});
