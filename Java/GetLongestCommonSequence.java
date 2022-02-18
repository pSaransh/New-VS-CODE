package Java;

import java.util.Scanner;

public class GetLongestCommonSequence {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int size = input.nextInt();
        String[] array = new String[size];
        for(int i=0; i<size; i++)
            array[i] = input.next();

        for(String i:array)
            System.out.println(i);
        System.out.println(getLongestCommonSequence(array));
        input.close();
    }
    public static String getLongestCommonSequence(String[] array){
        String commonSequence = "";
        for(int i = 0; i<array.length-1; i++)
        {
            for(int j = 0; j<array[i].length()-1 && j<array[i+1].length()-1; j++)
            {
                if(array[i].substring(0, j+1).equals(array[i+1].substring(0,j+1))){
                    if(commonSequence.length()>=array[i].substring(0, j+1).length()){
                        commonSequence+=array[i].substring(0, j+1);
                    }
                }
                System.out.println(commonSequence);
            }
        }
        return commonSequence;
    }
}
