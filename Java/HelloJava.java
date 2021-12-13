package Java;

import java.util.*;

public class HelloJava {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
               sc.close();
    }
    static String angrams(String s1,String s2)
    {
        String s3="";
        for(int i=0;i<s1.length();i++)
        {
            if(s2.indexOf(s1.charAt(i))==-1)
            {
                s3=s3+s1.charAt(i);
            }
        }   
}
