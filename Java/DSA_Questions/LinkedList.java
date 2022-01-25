package Java.DSA_Questions;
// import java.util.*;
public class LinkedList {
    Node headNode;
    public Node addNode(int data){
        Node newNode = new Node(data);
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
    public Node addNode(int data,int position){
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
    }
    
}
