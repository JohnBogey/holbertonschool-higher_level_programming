#!/usr/bin/node
exports.logMe = function (item) {
  console.log(argsAlreadyPrinted + ': ' + item);
  argsAlreadyPrinted += 1;
};
let argsAlreadyPrinted = 0;
