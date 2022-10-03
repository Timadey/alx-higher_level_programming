#!/usr/bin/node
const arg = process.argv;
if (isNaN(arg[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < parseInt(arg[2]); index++) {
    console.log('C is fun');
  }
}
