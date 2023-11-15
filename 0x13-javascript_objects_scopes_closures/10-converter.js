#!/usr/bin/node

// Converts number from base 10 to another

exports.converter = function (base) {
  function myConverter (n) {
    return n.toString(base);
  }

  return myConverter;
};
