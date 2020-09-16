#!/usr/bin/node
let number;
if (process.argv.length > 2) {
  number = parseInt(process.argv[2]);

  if (!isNaN(number)) {
    console.log('My number: ' + process.argv[2]);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
