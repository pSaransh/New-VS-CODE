package Java;
//import java.util.*;
public class Solution {
    
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        System.out.println(new Solution().updateString(n));
    }
    boolean updateString(int n){
        double pr = 1+4*n;
        return Math.sqrt(pr)%1==0.0;
    }
}