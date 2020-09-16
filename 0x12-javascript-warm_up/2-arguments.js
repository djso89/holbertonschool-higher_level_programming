#!/usr/bin/node
const input = process.argv;
const inputs = input.length;
if (inputs === 2) {
  console.log('No argument');
} else if (inputs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
