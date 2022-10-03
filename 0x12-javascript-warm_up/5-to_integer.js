#!/usr/bin/env node
import process from 'node:process';
const arg = process.argv;
const num = arg[2];
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
