public class CatchTheBastard {
    public static void main(String[] args) {
        int[] arr1 = {1,2,3,4};
        int[] arr2 = {1,2,3};
        System.out.println(new CatchTheBastard().getTheBastardLocation(arr1,arr2));
    }
    public int getTheBastardLocation(int[] arr1, int[] arr2){
        int i=0;
        boolean flag = false;
        int max = arr1.length>=arr2.length?arr1.length:arr2.length;
        try{
            for (i=0; i < max; i++) {
                if(arr1[i]==arr2[i]){   
                    flag=true;
                    continue;}
                else{
                    return i;
                }
            }
        }catch(Exception e){
            //do something
            return i;
        }
        return flag?-1:-1;
    }
}
