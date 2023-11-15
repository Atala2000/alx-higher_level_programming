#!/usr/bin/node

// Returns occuence numbers

exports.nbOccurences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
