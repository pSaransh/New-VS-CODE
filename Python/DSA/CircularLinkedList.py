import random as r

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next=None

class CircularLinkedList:
    def __init__(self)->None: 
        self.head = None
        
    def append(self,val,pos=None):
        newNode = Node(val)
        point1 = self.head
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
        elif pos==0:
            newNode.next = self.head
            while point1.next is not self.head:
                point1 = point1.next
            point1.next = newNode
            self.head = newNode
        elif pos is not None and pos!=0:
            point2 = Node()
            posChecker = 0
            while point1.next is not self.head and posChecker<pos-1:
                point2 = point1
                point1 = point1.next
                posChecker+=1
            point2.next = newNode
            newNode.next = point1        
        else:
            point1 = self.head
            while point1.next is not self.head:
                point1 = point1.next
            point1.next = newNode
            newNode.next = self.head
        return self.head
    
    def pop(self,pos=None):
        point1 = self.head
        if pos==0:
            while point1.next is not self.head:
                point1 = point1.next
            self.head = self.head.next
            point1.next = self.head
        elif pos is not None and pos!=0:
            point2 = Node()
            posChecker = 0
            while point1.next is not None and posChecker<pos-1:
                point2 =  point1
                point1 = point1.next
                posChecker+=1
            point2.next = point1.next    
        else:
            point2 = Node()
            while point1.next is not self.head:
                point2 =  point1
                point1 = point1.next
            point2.next=self.head
        return self.head

    def getHead(self):
        return self.head

    def lookup(self,key):
        point1 = self.head
        counter = 0
        while point1.next is not self.head:
            counter+=1
            if point1.data==key: return True,counter 
            point1 = point1.next
        return False,-1

    def traverse(self) -> None:
        point1 = self.head
        while point1:
            print(point1.data,end=" ")
            point1 = point1.next
            if point1 is self.head: break
        print()

def main():
    ll1 = CircularLinkedList()
    for i in range(1,11):
        foo = r.randint(10,100)
        ll1.append(foo)
    ll1.append(7,0)
    ll1.append(43,5)
    ll1.traverse()
    ll1.pop(5)
    ll1.sortList() 
    ll1.traverse()
    t = ll1.lookup(int(input()))
    if t[0]:
        print('Found at:',t[1],'❤️')
    else: print('😒')

main()
