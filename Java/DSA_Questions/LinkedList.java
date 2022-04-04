class Node{
    int data;
    Node next;
}
// import java.util.*;
public class LinkedList {
    Node headNode = null;
    public Node addNode(int data){
        Node newNode = new Node();
        if(headNode==null){
            headNode = newNode;
            headNode.next=null;
        }
        else{
            Node travelingNode = headNode;
            while(travelingNode.next!=null){
                travelingNode = headNode.next;
            }
            travelingNode = newNode;
            travelingNode.next = null;
        }
        return headNode;
    }
    /*public Node addNode(int data,int position){
        Node newNode = new Node(data);
        int positionCount=0;
        if(headNode==null){
            headNode = newNode;
            headNode.next=null;
        }
        else{
            Node travellingNode = headNode;
            while(travellingNode.next!=null&&positionCount<position){
                positionCount+=1;
                travellingNode = headNode.next;
            }
            travellingNode = newNode;
            travellingNode.next = null;
        }
        return headNode;
    }*/
    public void traverse(){
        if(headNode==null) return;
        else{
            Node ptr = headNode;
            //ptr = headNode;
            while(ptr.next != null){
                System.out.print(ptr.data+" ");
                ptr = ptr.next;
            }
        }
    }
    public static void main(String[] args) {
        LinkedList add = new LinkedList();
        for (int i = 0; i < 10 ; i++) {
            add.addNode(i);
        }
        add.traverse();
    }
}
