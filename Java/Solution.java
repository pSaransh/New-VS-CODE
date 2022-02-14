package Java;
import java.util.*;
/**
 * Solution
**/
class Solution{
	public static void main(String[] args)
    {
        //input
        Scanner sc = new Scanner(System.in);
        String instr1 = sc.next();
        String instr2 = sc.next();
        String fake_innum = sc.next();
        int innum = Integer.parseInt(fake_innum);
        sc.close();
        //building logic
        System.out.println(someFunction(instr1,instr2,innum));   
    }
    public static String someFunction(String instr1, String instr2, int innum)
    {
        StringBuffer sb1 = new StringBuffer(instr1);
        StringBuffer sb2 = new StringBuffer(instr2);
        StringBuffer output = new StringBuffer();
        if(innum>instr1.length()||innum>instr2.length())
        {
            output.append(sb1);
            output.append(sb2);
            return output.toString();
        }
        else
        {
            for(int i=0; i<instr1.length() || i<instr2.length(); i++)
            {
                if(i+innum<instr1.length() || i+innum<instr2.length())
                output.append(instr1.substring(i, i+innum));
                output.append(instr2.substring(i, i+innum));
            }
        }
        return output.toString();
    }
}
