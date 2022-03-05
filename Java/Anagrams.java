import java.util.*;
public class Anagrams{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        System.out.println(checkAnagrams(s1,s2));
        sc.close();
    }
    static String checkAnagrams(String s1, String s2)
    {
        if(s1.length()!=s2.length())
            return "Strings are not anagram.";
        char[] arrS1 = s1.toCharArray();
        char[] arrS2 = s2.toCharArray();
        Arrays.sort(arrS1);
        Arrays.sort(arrS2);
        for(int i=0; i<arrS1.length; i++)
                if(arrS1[i]!=arrS2[i])
                    return "String are not anagram.";
        return "Strings are anagram.";
    }
}