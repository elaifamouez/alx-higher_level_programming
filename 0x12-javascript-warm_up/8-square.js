#!/usr/bin/node
if ((isNaN(process.argv[2])) === false) {
  let row = '';
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    row += 'X';
  }
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
