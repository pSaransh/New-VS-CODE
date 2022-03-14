/**
 * *Beta
 *  !: Implement this class
 * 
 */
abstract class Shape{
	int l,b;
	abstract void printArea();
}
class Rect extends Shape {
	void printArea(){
		System.out.println(super.l*super.b);
	}
}

class Tri extends Shape {
	void printArea(){
		System.out.println(0.5*super.l*super.b);
	}
}

class Circle extends Shape {
	void printArea(){
		System.out.println(Math.PI*super.l*super.l);
	}
}

public class Beta {
	public static void main(String[] args){
		Rect r1 = new Rect();
		r1.l=3; r1.b=4;
		r1.printArea();
		Tri t1 = new Tri();
		t1.l=3; t1.b=4;
		t1.printArea();
		Circle c1 = new Circle();
		c1.l=3; c1.b=4;
		c1.printArea();
		
	}
}
