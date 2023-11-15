#!/usr/bin/node

const dict = require('./101-data').dict;
const newObj = {};

Object.keys(dict).forEach(function (key) {
  if (!Array.isArray(newObj[dict[key]])) {
    newObj[dict[key]] = [];
  }
  newObj[dict[key]].push(key);
});


console.log(newObj);
