#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (error, request, body) {
  if (error) {
    console.log(error);
  } else {
    const dos = JSON.parse(body);
    const outs = {};
    for (let i = 0; i < dos.length; i++) {
      if (dos[i].completed) {
        if (!(dos[i].userId in outs)) {
          outs[dos[i].userId] = 0;
        } outs[dos[i].userId] += 1;
      }
    }
    console.log(outs);
  }
});
