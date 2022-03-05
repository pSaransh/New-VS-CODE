public class trialingZeros {
    public static void main(String[] args) {
       int num=10;
       int zeroCount=0;
       for(int i=1; i<=num;i++)
       {
                zeroCount+=getFivePower(i);
       }
       System.out.println(zeroCount);
       Runtime.getRuntime().exit(1);
    }
    static int getFivePower(int n)
    {
        int flag=0;
        int nC = n;
        while(nC>0)
        {
            if(nC%5==0)
                flag+=1;
            nC/=5;
        }
        return flag;
    }
}
