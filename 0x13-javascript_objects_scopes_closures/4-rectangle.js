#!/usr/bin/node
// Empty class rectangle

module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; ++i) {
        let j = 0;
        for (; j < this.width; ++j) {
          process.stdout.write('X');
        }
        if (j === this.width) {
          console.log('');
        }
      }
    } else {
      console.log('Invalid width or height');
    }
  }
};
