package Java;
import java.util.*;
class Node{
    int data;
    Node next;   
}
class Stack{
    private Node top;
    public Stack(){
        this.top=null;
    }
    public void push(int data){
        Node node = new Node();
        if(node==null){
            System.out.println("Heap Overflow.");
            return;
        }
        node.data = data;
        node.next=top;
        top = node;
    }
    public boolean isEmpty(){
        return top==null;
    }
    public int peek(){
        if(!isEmpty())
            return top.data;
        return Integer.MIN_VALUE;

    }
    public int pop(){
        if(top==null){
            System.out.println("Stack is empty.");
            return Integer.MIN_VALUE;
        }
        int popped = top.data;
        top = top.next;
        return popped;
    }
    public boolean search(int key){
        if(top==null)
            return false;
        Node ptr = new Node();
        ptr=top;
        while(ptr!=null)
        {
            if(top.data==key)
                return true;
            ptr=top.next;
        }
        return false;
    }
    public void display(){
        if(top==null)
            return;
        Node ptr = new Node();
        ptr=top;
        while(ptr!=null)
        {
            System.out.print(ptr.data+" ");
            ptr=top.next;
        }
        return;
    }
}
public class Stack_Implementation{
    public static void main(String[] args) {
        
    }
}