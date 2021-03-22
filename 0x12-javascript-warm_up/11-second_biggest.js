#!/usr/bin/node

let secondMax = 0;
const args = process.argv.slice(1);
if (args.length > 1) {
  args.sort();
  secondMax = args[args.length - 2];
}
console.log(secondMax);
