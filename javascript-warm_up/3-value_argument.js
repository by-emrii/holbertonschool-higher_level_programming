#!/usr/bin/node
const arg = process.argv[2]; // first arg passed after node path and script path

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
