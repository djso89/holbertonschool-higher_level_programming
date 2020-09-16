#!/usr/bin/node

function secondbig (arr) {
  if (arr.length === 1 || arr.length === 0) return 0;
  let top = -Infinity;
  let top1 = -Infinity;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > top) {
      top1 = top;
      top = arr[i];
    } else if (top > arr[i] > top1) {
      top1 = arr[i];
    }
  }
  return top1;
}

const arr = process.argv.slice(2, process.argv.length).map(Number);
console.log(secondbig(arr));
