let x,y,step=1;
let px=0, py=0;
let stepSize = 20;
let numSteps = 1;
let state = 0;
let turnCounter = 0;
let r=0,g=0,b=0;
let totalSteps;
function setup() {
  createCanvas(1000, 1000);
  x = width/2;
  y = height/2;
  //background(0);
  const cols  = width/stepSize;
  const rows = height/stepSize;
  totalSteps = cols * rows;
  px=x;
  py=y;
}

function draw() {
  

  fill(255,0,0);
  stroke(255,0,0);
  if(isPrime(step))
  circle(x,y,stepSize*0.25);
  stroke(255,0,0);
  //if(isPrime(step))
  line(x,y,px,py);
  px=x;
  py=y;
  switch(state){
    case 0: x += stepSize;
      break;
    case 1: y -= stepSize;
      break;
    case 2: x -= stepSize;
      break;
    case 3: y += stepSize;
      break;
  }
  if(step%numSteps==0){
    state = (state+1) % 4;
    turnCounter+=1;
    if(turnCounter % 2 == 0){numSteps += 1;}
  }
  step+=1;
  if(step > totalSteps) noLoop();
  //frameRate(1);
}
const isPrime = (number) => {
  let count = 0;
  for(let i=1; i <= number; i++){
    if(number % i == 0) count+=1; 
  }
  return count==2;
}