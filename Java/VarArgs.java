public class VarArgs {
    public static void main(String[] args){
        A obj1 = new A();
        System.out.println(obj1.add(2,3,345,767,23,1324,56));
        B obj2 = new B()
                    {
                        public void show(){
                            System.out.println("Hello World");
                        }
                    };
        obj2.show();

    }
}
class A{
    public int add(int... b){
        int sum=0;
        for(int i:b) sum+=i;
        return sum;
    }
}
interface B{
    void show();
}
