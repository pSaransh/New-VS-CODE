#!/usr/bin/env node
function printFactors(n){
    let arr = []
    for(let i=1;i<n;i++)
        if(n%i==0)
            arr.push(i)
    
    console.log(arr);
}
const program = require('commander');
program.version('1.0.0').description('Prints factor of the provided number')
program
    .option('-n <number>','Insert Number')
    .parse()
const {n} = program.opts();
printFactors(n)