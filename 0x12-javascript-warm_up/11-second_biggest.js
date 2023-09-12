#!/usr/bin/node
if (process.argv[3]) {
  let biggest = parseInt(process.argv[2]);
  let runnerUp = NaN;
  let temp;
  for (let i = 3; i < process.argv.length; i++) {
    temp = parseInt(process.argv[i]);
    if (temp > biggest) {
      runnerUp = biggest;
      biggest = temp;
    } else if (isNaN(runnerUp)) {
      runnerUp = temp;
    } else if (temp > runnerUp) {
      runnerUp = temp;
    }
  }
  console.log(runnerUp);
} else {
  console.log(0);
}
