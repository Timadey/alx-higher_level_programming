#!/usr/bin/node
let arg = process.argv;
arg = arg.slice(2, 4);
arg = arg.join(' is ');
console.log(arg);
