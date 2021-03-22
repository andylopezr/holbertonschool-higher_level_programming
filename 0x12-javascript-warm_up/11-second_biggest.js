#!/usr/bin/node

let secondMax = 0;
let args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  secondMax = args[args.length - 2];
}
console.log(secondMax);
