interface BankInterface1{
    static void show(){
        System.out.println("LOL I'm a method in interface but I'm not abstract!! In your face you developer!!");
    }
    float rateOfInterest();
}
abstract class BankInterface2 implements BankInterface1{
    @Override
    public float rateOfInterest(){
        return 0.9865f;
    }
}
class SBI implements BankInterface1{
    @Override
    public float rateOfInterest(){
        return 9.75f;
    }    
}
public class WEB_T_CT1{
    public static void main(String[] args) {
        SBI sbi1 = new SBI();
        BankInterface1.show();
        System.out.println(sbi1.rateOfInterest());
    }

}