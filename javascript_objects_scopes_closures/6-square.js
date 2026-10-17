#!/usr/bin/node
const Square = require('./5-square');

class MySquare extends Square {
  charPrint (c) {
    const ch = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(ch.repeat(this.width));
    }
  }
}

module.exports = MySquare;
