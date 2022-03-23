/** This function sets up our sketch. */
function setup() {
    createCanvas(600, 600);
}
/** This function redraws the sketch multiple times a second. */
function draw() {
    background(0);

    stroke(255);
    
    // strokeWeight(24);
    // point(0,300);
    // point(mouseX,mouseY);
    // point(mouseX,mouseY);
    // point(600,300);
    // let point1 = point(30,300);
    // let point2 = point(570,200);
    // strokeWeight(4);
    // //noFill();
    // line(mouseX,mouseY,570,100);
    //bezier(0, 300, mouseX, mouseY, mouseX, mouseY, 600, 300);
}

function mouseDragged() {
    point(mouseX,mouseY);
    // prevent default
    return false;
  }