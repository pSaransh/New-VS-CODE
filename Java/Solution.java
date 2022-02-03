package Java;
//import java.util.*;
public class Solution {
    
    public static void main(String[] args) {
        System.out.println(new Solution().newCondition(1000,2));
    }
    int newCondition(int n,int k){
        int count=0;
        for(int i=1; i<=n ;i++){
            /**
            If the following condition pass then add result from getTotalDivisions() to count.
            **/
            if(i%k==0){
                int result = getTotalDivisions(i, k, 0);
                count+=result;
            }
        }
        return count;
    }
    static int getTotalDivisions(int n, int k,int count)
    {
        /**
        This recursive function will calculate all the divisions possible between two numbers
        For Ex: n = 4 and k = 2
        It'll return 2 because 2 can divide 4, 2 times.
        For Ex: n = 6 and k = 2
        It'll return one.
        Rest is self-explanatory
        **/
        if(n<k) return count;
        else if(n%k==0){
            return getTotalDivisions(n/k, k, count+1);
        }
        return count;        
    }
}