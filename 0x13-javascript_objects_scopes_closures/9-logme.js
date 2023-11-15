#!/usr/bin/node

let flag = 0;

exports.logMe = function count (item) {
  console.log(`${flag}: ${item}`);
  flag += 1;
};
