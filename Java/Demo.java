import java.util.*;
public class Demo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n-1];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println(new Demo().getMissing(arr,n));
        sc.close();
    }
    int getMissing(int[] arr,int n){
        boolean flag=true;
        int returnVal = 0;
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]!=i+1)
            {
                returnVal = i+1;
                flag = false;
                break;
            }
        }
        if(flag){
            return arr[arr.length-1]+1;
        }
        return returnVal;
    }
} 
