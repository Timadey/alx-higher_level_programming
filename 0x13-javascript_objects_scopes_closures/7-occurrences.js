#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  list.forEach(elem => {
    if (elem === searchElement) {
      occurence++;
    }
  });
  return occurence;
};
