#!/usr/bin/node
import process from 'node:process';
let arg = process.argv;
arg = arg.slice(2, 4);
arg = arg.join(' is ');
console.log(arg);
