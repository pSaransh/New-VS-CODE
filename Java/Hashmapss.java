package Java;

import java.util.*;

public class Hashmapss {
    public static void main(String[] args) {
        HashMap<String,String> phonebook = new HashMap<String,String>();
        phonebook.put("Navin","8004908542");
        System.out.println(phonebook);
        System.out.println(phonebook.get("Navin"));
        ArrayList<Integer> newarry = new ArrayList<Integer>();
        newarry.add(3);
        newarry.add(4);
        System.out.println(newarry.contains(5));
    }
}