#!/usr/bin/node

const input = process.argv.length - 2;
if (input < 2) {
  console.log(0);
} else {
  const array = process.argv.slice(2);
  const sorted = array.sort();
  console.log(array[sorted.length - 2]);
}
