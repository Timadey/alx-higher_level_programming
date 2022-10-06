#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((elem, index) => {
  return elem * index;
});
console.log(list);
console.log(newList);
