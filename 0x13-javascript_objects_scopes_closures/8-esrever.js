exports.esrever = function (list) {
  let reversed = [];
  for (let i = list.length; i >= 0; i--) {
    reversed.push(list[i]);
  }
  reversed.shift();
  return reversed;
}
