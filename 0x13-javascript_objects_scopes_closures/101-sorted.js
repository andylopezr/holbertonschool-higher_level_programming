#!/usr/bin/node

const dict = require('./101-data').dict;

const newdict = {};
for (const uid in dict) {
  if (newdict[dict[uid]] === undefined) {
    newdict[dict[uid]] = [];
  }
  newdict[dict[uid]].push(uid);
}

console.log(newdict);
