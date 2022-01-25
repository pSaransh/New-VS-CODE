class Node:
    def __init__(self,data=None):
        self.data = data
        self.next=None

class LinkedList:
    def __init__(self,head)->None:
        self.head = head
    
    def append(self,val,pos=None):
        newNode = Node(val)
        point1 = self.head
        if self.head == None:
            self.head = newNode
        elif pos==0:
            newNode.next = self.head
            self.head = newNode
        elif pos is not None and pos!=0:
            point2 = Node()
            posChecker = 0
            while point1 is not None and posChecker<pos-2:
                point2 = point1
                point1 = point1.next
                posChecker+=1
            point2.next = newNode
            newNode.next = point1        
        else:
            while point1.next is not None:
                point1 = point1.next
            point1.next = newNode
        return self.head
    
    def pop(self,pos=None):
        point1 = self.head
        if pos==0:
            self.head = self.head.next
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
        if left == None:
            return right
        if right == None:
            return left
        if left.data <= right.data:
            result = left
            result.next = self.sortedMerge(left.next, right)
        else:
            result = right
            result.next = self.sortedMerge(left, right.next)
        return result

    def mergeSort(self, h):
        if h == None or h.next == None:
            return h
        middle = self.getMiddle(h)
        nextToMiddle = middle.next
        middle.next = None
        left = self.mergeSort(h)
        right = self.mergeSort(nextToMiddle)
        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def getMiddle(self, head):
        if (head == None):
            return head
        slow = head
        fast = head
        while (fast.next != None and fast.next.next != None):
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
    ll1 = LinkedList(Node(10))
    for i in range(2,11):
        ll1.append(i*10)
    ll1.traverse()
    ll1.pop(4)
    ll1.traverse()
    ll1.append(110,5)
    ll1.sortList()
    ll1.traverse()
    t = ll1.lookup(int(input()))
    if t[0]:
        print('Found at:',t[1],'❤️')
    else: print('😒')

main()