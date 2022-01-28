package Java;
//import java.util.*;
public class Solution {
    
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        System.out.println(new Solution().isHeteromecic(n));
    }
    boolean isHeteromecic(int c){
        return Math.sqrt(1+4*c)%1==0.0;
    }
}