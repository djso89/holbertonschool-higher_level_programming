#!/usr/bin/node
exports.esrever = function (list) {
  const out = [];
  while (list.length) {
    out.push(list.pop());
  }

  return out;
};
