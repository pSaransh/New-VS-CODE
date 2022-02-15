package Java;
import java.util.*;
/**
 * Solution
**/
class Solution{
	public static void main(String[] args)
    {
        //input
        String[] stringArr = {"flower","fling","flush"};
        System.out.println(new Solution().someFunctionThatWillDoShit(stringArr));

    }
    // boolean startsWith(String compareWith, String comparingWithThis)
    // {
    //     if(compareWith.startsWith(comparingWithThis))
    //         return true;
    //     return false;
    // }
    void compareTwoStrings(String firstString, String secondString)
    {
        
    }
    String someFunctionThatWillDoShit(String[] stringArr)
    {
        StringBuffer sb1 = new StringBuffer(stringArr[0]);
        StringBuffer sb2 = new StringBuffer(stringArr[1]);
        int lessLen = sb1.length()<sb2.length()?sb1.length():sb2.length();
        StringBuffer output = new StringBuffer();
        for(int i=0; i < lessLen; i++)
        {
            if(sb1.charAt(i)==sb2.charAt(i))
                output.append(sb1.charAt(i));
        }
        String commonSequence = output.toString();
        for(int i=2; i<stringArr.length; i++)
        {
            compareTwoStrings(stringArr[i],commonSequence);
        }
        return output.toString();
    }
}
