#!/usr/bin/node
import process from 'node:process';
const arg = process.argv;
if (!arg[2]) {
  console.log('No argument');
} else {
  console.log(arg[2]);
}
