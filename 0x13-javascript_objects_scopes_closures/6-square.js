#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  // Prints the square using character 'c'
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      for (let y = 0; y < this.width; y++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Square;
