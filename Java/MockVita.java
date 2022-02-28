import java.util.*;
class A{
    Scanner sc = new Scanner(System.in);
    double pi = 3.141592653589793;
    private int r1=0,r2=0,s1=0,s2=0,t=0,d=0;
    void getInput(){
        r1 = sc.nextInt();
        r2 = sc.nextInt();
        s1 = sc.nextInt();
        s2 = sc.nextInt();
        t = sc.nextInt();
        d = sc.nextInt();
    }
    boolean dCompare()
    {
        if(d<=r1+r2) return true;
        if(d>r1+r2) return false;
        return false;
    }
    void calculateCrash(){
        if(!dCompare()){
            System.out.println("No crash");
            return;
        }
        System.out.println("Enter Input: ");
        getInput();
        System.out.println(getArcLen());
        ArrayList<Double> tS = m1AtE();
        System.out.println("m1AtE");
        print(tS);
        tS.clear();
        tS = m1AtF();
        System.out.println("m1AtF");
        print(tS);
        tS.clear();
        tS = m2AtE();
        System.out.println("m2AtE");
        print(tS);
        tS.clear();
        tS = m2AtF();
        System.out.println("m2AtF");
        print(tS);
        tS.clear();
    }
    void print(ArrayList<Double> tS){
        for(Double i: tS)
            System.out.print(i+" ");
        System.out.println();
    }
    double getArcLen(){
        double angle = ((this.r1*this.r1-this.r2*this.r2)+this.d*this.d)/(2*this.r1*this.d);
        return Math.toRadians(2*Math.acos(angle));
    }
    ArrayList<Double> m1AtE(){
        double time = 0;
        double circumference = 2*pi*r1;
        ArrayList<Double> timestamps = new ArrayList<Double>();
        while(time<t){
            time+=(circumference/s1);
            timestamps.add(time);
        }
        return timestamps;
    }
    ArrayList<Double> m1AtF(){
        double arcLen = getArcLen();
        double time = arcLen/s1;
        double circumference = 2*pi*r1;
        ArrayList<Double> timestamps = new ArrayList<Double>();
        timestamps.add(time);
        while(time<t){
            time+=(arcLen+circumference/s1);
            timestamps.add(time);
        }
        return timestamps;
    }
    ArrayList<Double> m2AtF(){
        double time = 0;
        double circumference = 2*pi*r2;
        ArrayList<Double> timestamps = new ArrayList<Double>();
        while(time<t){
            time+=(circumference/s2);
            timestamps.add(time);
        }
        return timestamps;
    }
    ArrayList<Double> m2AtE(){
        double arcLen = getArcLen();
        double time = arcLen/s2;
        double circumference = 2*pi*r2;
        ArrayList<Double> timestamps = new ArrayList<Double>();
        timestamps.add(time);
        while(time<t){
            time+=(arcLen/s2);
            timestamps.add(time);
        }
        return timestamps;
    }    
}
public class MockVita {
    public static void main(String[] args) {
        A obj1 = new A();
        System.out.println(20*Math.toRadians(2*Math.acos(893/920)));
        //obj1.calculateCrash();
    }
}
