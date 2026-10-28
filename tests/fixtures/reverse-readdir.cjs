// Exercise the real generator with a different filesystem enumeration order.
const fs=require('node:fs');
const original=fs.readdirSync;
fs.readdirSync=function(...args){
  return original.apply(this,args).reverse();
};
