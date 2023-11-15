#!/usr/bin/node

let size = parseInt(process.argv[2]);
if (isNaN(size) || process.argv[2] === undefined) {
  console.log('Missing size');
}
let psr = 'X';
for (let i = 0; i < size; i++) {
  psr += 'X';
}
while (size > 0) {
  console.log(psr);
  size--;
}
