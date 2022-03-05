// String s = "His life was supposed to be simple but there's just one attribute that he's proud of. He was born in Hidden Leaf Village. His parents are shinobi and was killed in Nine-Tail Attack, the day on which a child of prophecy was born-Naruto. With Naruto he also grow up as a father, as a guardian. Although he was just a teacher of Naruto but he meant so much for Naruto. During childhood of Naruto, he always looked up for him and help him to become a better person. He and Ichiraku-Ramen were the only shield that keep Naruto away from all the hate imposed by villagers. He cried when the same people who used to hate Naruto, calles him \"Hero of the Hidden Leaf\", his eyes were filled with tears and there were several flashbacks running through his mind. It matters that Naruto's struggle is important but what's most important that Naruto always have someone on his side. His name is Iruka Umino.";

import java.util.*;
public class Regular_Expressions {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        /*
        Regular Expressions - to check for a specific pattern in the given text or search some text from a given file.
        \d - [0-9]
        \D - [^0-9]
        \s - [ \t\n\f\r]
        \S - [^ \t\n\f\r]
        \w - [a-zA-Z0-9_]
        \W - [^\w]
        * - zero or more
        + - one or more
        ^ - begin with | not included
        $ - end with
        ? - optional
        {n,} - at least n times
        {n,m} - at least n times, atmost m times
        */
        //to check digits
        String digits = "\\d+";
        boolean flag = false;
        do{
            System.out.println("Input numbers: ");
            String number = sc.next();
            flag = number.matches(digits);
            if(!flag)
                System.out.println("Invalid");
            else
                System.out.println("Valid");
        }
        while(!flag);

        //to check date
        String dateCheck = "(3?[0-1]|[0-2][0-9])-(0[0-9]|1[1-2])-([1-2][0-9]{3})";
        do{
            System.out.println("Input date: ");
            String number = sc.next();
            flag = number.matches(dateCheck);
            if(!flag)
                System.out.println("Invalid");
            else
                System.out.println("Valid");
        }
        while(!flag);
        sc.close();
    }   
}
