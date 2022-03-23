public class LeetCode {
    public static void main(String[] args) {
        new LeetCode().generateStrings(5,73);
    }
    public void generateStrings(int n, int k){
        //case 1 if k <= 26
        int nCopy = n;
        if(k <= 26){
            String str = "";
            for(;nCopy>=1;){
                
            }
        }
    }
    public int getPlaceValue(char ch){
        int asciiVal = Character.getNumericValue(ch);
        return asciiVal-96;
    }
}
