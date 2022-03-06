package DSA_Questions;
public class Node {
    Integer valInteger;
    String valString;
    Character valCharacter;
    Double valDouble;
    Node next = null;
    Node(Integer valInteger){
        this.valInteger = valInteger;
        this.next = null;
    }
    Node(String valString){
        this.valString = valString;
        this.next = null;
    }
    Node(Character valCharacter){
        this.valCharacter = valCharacter;
        this.next = null;
    }
    Node(Double valDouble){
        this.valDouble = valDouble;
        this.next = null;
    }
    
    // Node(Integer valInteger, Node next){
    //     this.valInteger = valInteger;
    //     this.next = next;
    // }
    // Node(String valString, Node next){
    //     this.valString = valString;
    //     this.next = next;
    // }
    // Node(Character valCharacter, Node next){
    //     this.valCharacter = valCharacter;
    //     this.next = next;
    // }
    // Node(Double valDouble, Node next){
    //     this.valDouble = valDouble;
    //     this.next = next;
    // }
}
