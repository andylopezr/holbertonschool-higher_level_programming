#!/usr/bin/node

module.exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const ele in list) {
    if (list[ele] === searchElement) {
      count++;
    }
  }
  return count;
};
