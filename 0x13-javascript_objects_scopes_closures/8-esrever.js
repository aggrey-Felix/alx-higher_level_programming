#!/usr/bin/node
/*
*Write a function that returns the reversed version of a list
*Prototype: exports.esrever = function (list)
*You are not allow to use the built-in method reverse
*/
exports.esrever = function (list) {
  const rev = [];
  for (let i = 0; i < list.length; i++) {
    rev.unshift(list[i]);
  }
  return rev;
};
