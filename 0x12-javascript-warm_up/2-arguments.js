#!/usr/bin/env node
import process from 'node:process';
const arg = process.argv;
if (arg.length === 2) {
  console.log('No argument found');
} else if (arg.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
