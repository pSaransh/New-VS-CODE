package Java;
import java.util.*;
public class RearrangeDigs {

   public static void main(String[] args) {
        List<Integer> list=new ArrayList<Integer>();  
        int[] arr = {515, 341, 98, 44, 211};
        for(int i:arr) list.add(i);
        new RearrangeDigs().reorderDigits(list,"desc");
       
   }
   void reorderDigits(List<Integer> list,String s)
   {
       List<Integer> arr = new ArrayList<Integer>();
       if(s=="asc"){
           for(Integer i:list)
           {
               Integer res = new RearrangeDigs().reArrangeInteger(i,1);
               arr.add(res);
           }
       }
       else{
            for(Integer i:list)
            {
                Integer res = new RearrangeDigs().reArrangeInteger(i,2);
                arr.add(res);
            }
       }
       new RearrangeDigs().printList(arr);
   }
   Integer reArrangeInteger(int item,int condition)
   {
       int res=0;
       
       ArrayList<Integer> lIntegers = new ArrayList<Integer>();
       if(condition==1)
       {
           while(item>0){
               int rem = item%10 ;
               lIntegers.add(rem);
               item/=10;
           }
           Collections.sort(lIntegers);
           for(int i:lIntegers){
               res = res*10+i;
           }
       }
       else{
            while(item>0){
                int rem = item%10 ;
                lIntegers.add(rem);
                item/=10;
            }
            Collections.sort(lIntegers,Collections.reverseOrder());
            for(int i:lIntegers){
                res = res*10+i;
            }
       }
       return res;
   }
   void printList(List<Integer> arr)
   {
       System.out.println(arr);
   }
}