import java.util.ArrayList;

public class subArrays {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4};
        //ArrayList<ArrayList<Integer>> subArrys = new ArrayList<ArrayList<Integer>>();
        //ArrayList<Integer> subSubs = new ArrayList<Integer>();
        int offset=1;
        for(int i=0; i<arr.length;i++)
        {
            for(int j=i; j<arr.length-offset+1; j++)
            {
                for(int k=j; k<=j+offset-1; k++)
                    System.out.print(arr[k]+" ");
                System.out.println();
            }
            //offset
            offset+=1;
        }
        /**
         * 1 i=0 j=null
         * 2 i=0 j=null
         * 3 i=0 j=null
         * 4 i=0 j=null
         * 1,2 i=0,j=i+1
         * 2,3 i=1,j=i+1
         * 3,4 i=2,j=j+1
         * 1,2,3 i=0 to j=i+2
         * 2,3,4 i=1 to j=i+2
         */
        //int[][] subArray = new int[arr.length][arr.length];
        // for(int i=0; i<arr.length; i++)
        //     subSubs.add(arr[i]);
        // subArrys.add(subSubs);
        //System.out.println(subSubs);
        // subSubs.clear();
        // System.out.println(subArrys);
        // for(int i=0; i<arr.length-1; i++)
        // {
        //     subSubs.add(arr[i]);
        //     subSubs.add(arr[i+1]);
        //     subArrys.add(subSubs);
        //     subSubs.clear();
        // }
        // for(int i=0; i<arr.length-1; i++)
        // {
        //     for(int j=0; j<i; j++)
        //     {
        //         subSubs.add(arr[i+j]);
        //     }
        //     subArrys.add(subSubs);
        //     subSubs.clear();
        // }
    }
}
