// //code hoisting
// smallTipper("200")
// //smallTipper is a function and functions are scanned and made available globally by global context
// function smallTipper(bill){
//     console.log(parseInt(bill)+5);
// }
// //bigTipper("200")
// //this will give error:
// //TypeError : bigTipper is not defined
// //here bigTipper is a variable and not a function, also variables are scanned by global context and made undefined
// //this is called code hoisting
// var bigTipper = function (bill) {
//     console.log(parseInt(bill)+15);
// };
// bigTipper("200")
// console.log(r);
// const r = "Bruno"

//lets handle this
// for a regular function call this points to window/global object
// console.log(this); notebook sucks
//IIFE
//Self-Executing Anonymous Functions
//map

//Maps
//inheritance

const uno = () => {
  console.log("I am One.");
};
const dos = () => {
  setTimeout(() => {
    console.log("I am lazy...");
  }, 3000);
  console.log("I am Two.");
};  
const tres = () => {
  console.log("I am Three.");
};
uno();
dos();
tres();
