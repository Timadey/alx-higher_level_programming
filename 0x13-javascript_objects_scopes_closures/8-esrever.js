#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  const len = list.length - 1;
  for (let x = len; x > -1; x--) {
    newList.push(list[x]);
  }
  return newList;
};
