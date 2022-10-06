#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Print the Rectangle using the character
  // 'X'
  print () {
    for (let x = 0; x < this.height; x++) {
      for (let y = 0; y < this.width; y++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }

  // Exchange the width and the height of
  // the Rectangle
  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  // Multiply the width and height of the Rectangle
  // by 2
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
