var int1 = 3
var int2 = 13
const getSumOfRange = (n,m) => {
    let sum=0
    for(let i=n; i<=m; i++)
        sum+=i
    return Math.ceil(Math.atan(sum)) 
}
console.log(getSumOfRange(int1,int2));