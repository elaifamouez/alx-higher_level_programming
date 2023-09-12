#!/usr/bin/node
function recurse (a) {
  if (a === 1) {
    return 1;
  } else {
    return a * recurse(a - 1);
  }
}
if (isNaN(process.argv[2])) {
  console.log(recurse(1));
} else if (parseInt(process.argv[2]) >= 1) {
  console.log(recurse(parseInt(process.argv[2])));
}
