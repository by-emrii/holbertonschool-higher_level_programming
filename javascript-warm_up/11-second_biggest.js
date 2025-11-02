#!/usr/bin/node
const args = process.argv.slice(2).map(x => parseInt(x, 10)); // map - convert str to int

if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a); // sort descending
  console.log(args[1]); // second biggest
}
