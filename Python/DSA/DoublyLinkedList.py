class Node:
    def __init__(self,data=None):
        self.data = data
        self.next=None
        self.prev = None

class DoublyLinkedLst:
    def __init__(self)->None:
        self.head = None
    
    def append(self,val,pos=None):
        newNode = Node(val)
        point1 = self.head
        if self.head is None:
            self.head = newNode
            newNode.prev = self.head
        elif pos==0:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        elif pos is not None and pos!=0:
            point2 = Node()
            posChecker = 0
            while point1 is not None and posChecker<pos-2:
                point2 = point1
                point1 = point1.next
                posChecker+=1
            newNode.prev = point2        
            point2.next = newNode
            newNode.next = point1
            point1.prev = newNode
        else:
            while point1.next is not None:
                point1 = point1.next
            point1.next = newNode
            newNode.prev = point1
        return self.head
    
    def pop(self,pos=None):
        point1 = self.head
        if pos==0:
            self.head = self.head.next
            self.head.prev = None
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
            while point1.next is not None:
                point2 =  point1
                point1 = point1.next
            point2.next=None
        return self.head

    def getHead(self):
        return self.head
    def getTail(self):
        point1 = Node()
        point1 = self.head
        
    def lookup(self,key):
        point1 = self.head
        counter = 0
        while point1 is not None:
            counter+=1
            if point1.data==key: return True,counter 
            point1 = point1.next
        return False,-1

    def sortList(self):
        self.head = self.mergeSort(self.head)
        return self.head

    def sortedMerge(self, left, right):
        result = None
        if left is None:
            return right
        if right is None:
            return left
        if left.data <= right.data:
            result = left
            result.next = self.sortedMerge(left.next, right)
        else:
            result = right
            result.next = self.sortedMerge(left, right.next)
        return result

    def mergeSort(self, h):
        if h is None or h.next is None:
            return h
        middle = self.getMiddle(h)
        nextToMiddle = middle.next
        middle.next = None
        left = self.mergeSort(h)
        right = self.mergeSort(nextToMiddle)
        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def getMiddle(self, head):
        if (head is None):
            return head
        slow = head
        fast = head
        while (fast.next is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def traverse(self) -> None:
        point1 = self.head
        while point1 is not None:
            print(point1.data,end=" ")
            point1 = point1.next
        print()

def main():
    ll1 = DoublyLinkedLst()
    items = [True,12,'H',"Python",20.98,['i',4,Node(10)]]
    for i in items:
        ll1.append(i)
    ll1.traverse()
    ll1.pop()
    ll1.traverse()
    ll1.append(110,5)
    ll1.traverse()
    t = ll1.lookup(int(input()))
    if t[0]:
        print('Found at:',t[1],'❤️')
    else: print('😒')

main()