
public class Beta {
        public static void main(String[] args) throws Exception {
        String s = "abcabbac";
        for(int i=0; i<s.length(); i++){
            StringPython getSubString = new StringPython(s.substring(i+1, s.length()));
            char realSubStr = s.charAt(i);
            String stringRealSubStr  = Character.toString(realSubStr);
            if(getSubString.in(stringRealSubStr)){
                s = s.substring(i+1, s.length());
            }
        }
        System.out.println(s);
    }
}