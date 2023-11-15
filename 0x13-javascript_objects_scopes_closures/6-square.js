#!/usr/bin/node

// creates square class

const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  constructor(size) {
    super(size, size);
  }

  double() {
    super.double();
  }

  charPrint(c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
};
