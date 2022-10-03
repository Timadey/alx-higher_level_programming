#!/usr/bin/env node
import process from 'node:process';
const arg = process.argv;
if (isNaN(arg[2])) {
  console.log('Missing size');
} else {
  const num = parseInt(arg[2]);
  for (let x = 0; x < num; x++) {
    for (let y = 0; y < num; y++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
