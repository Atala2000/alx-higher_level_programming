#!/usr/bin/node
// Executes func x
exports.callMeMoby = function (x, theFunction) {
  while (x-- > 0) {
    theFunction();
  }
};
