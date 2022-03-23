/*
 Problem: 
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

  Output:                     Expected Output:
  I am One.                       I am One.
  I am Two.                       I am Two.
  I am Three.                     I am Lazy...
  I am Lazy...                    I am Three
*/
const uno = () => {
  return "I am One.";
};
const dos = () => {
  return new Promise((resolve,reject) => {
    setTimeout(() => {
        resolve("I am lazy...");
      }, 3000);
      console.log('I am Two.');
  });
};
const tres = () => {
  return "I am Three.";
};

const callMe = async() => { //this function is going to behave asynchronously
    let valOne = uno();
    console.log(valOne);

    let valTwo = await dos(); //this function wants to wait
    console.log(valTwo);

    let valThree = tres();
    console.log(valThree);
}

callMe();
