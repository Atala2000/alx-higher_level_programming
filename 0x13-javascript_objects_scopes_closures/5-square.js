#!/usr/bin/node

// creates square class

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }
};
