#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const str = 'C is fun';
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log(str);
    i++;
  }
}
