package Java;
import java.util.*;
class HelloJava
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();
        System.out.println("Hello "+name);
        sc.close();
    }
}