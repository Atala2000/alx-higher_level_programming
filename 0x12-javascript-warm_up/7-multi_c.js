#!/usr/bin/node

let printX = parseInt(process.argv[2]);
if (isNaN(printX) || process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  while (printX > 0) {
    console.log('C is fun');
    printX--;
  }
}
