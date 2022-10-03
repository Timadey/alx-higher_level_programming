#!/usr/bin/env node
import process from 'node:process';
const arg = process.argv.slice(2);
if (arg.length === 0) {
  console.log(0);
} else if (arg.length === 1) {
  console.log(1);
} else {
  const nums = arg.map((elem) => { return parseInt(elem); });
  console.log(nums.sort((a, b) => b - a)[1]);
}
