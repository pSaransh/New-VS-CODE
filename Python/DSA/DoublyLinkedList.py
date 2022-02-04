class Node:
    def __init__(self,data=None):
        self.data = data
        self.next=None
        self.prev = None

class DoublyLinkedList:
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

    def getHead(self) -> Node:
        return self.head
    def getTail(self) -> Node:
        point1 = self.head
        while point1.next is not None:
            point1 = point1.next
        return point1
        
    def lookup(self,key) -> tuple:
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

    def getMiddle(self, head) -> Node:
        if (head is None):
            return head
        slow = head
        fast = head
        while (fast.next is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def isPalindrome(self) -> bool:
        current = self.head
        point1 = self.getTail()
        values1 = ""
        while current is not None:
            values1+=str(current.data)
            current = current.next
        point1 = self.getTail()
        values2 = ""
        while point1 is not self.head:
            values2+=str(point1.data)
            point1 = point1.prev
        values2+=str(point1.data)
        return values1==values2

    def printReverse(self):
        point1 = self.getTail()
        while point1 is not self.head:
            print(point1.data)
            point1 = point1.prev
        print()
    
    def merge(self,ll2):
        ll3 = DoublyLinkedList()
        selfLLHead = self.head
        secondLLHead = ll2.head
        while (selfLLHead is not None) and (secondLLHead is not None):
            if selfLLHead.data <= secondLLHead.data:
                ll3.append(selfLLHead.data)
                selfLLHead = selfLLHead.next
            else:
                ll3.append(secondLLHead.data)
                secondLLHead = secondLLHead.next
        while selfLLHead is not None:
            ll3.append(selfLLHead.data)
            selfLLHead = selfLLHead.next
        while secondLLHead is not None:
            ll3.append(secondLLHead.data)
            secondLLHead = secondLLHead.next
        return ll3

    def traverse(self) -> None:
        point1 = self.head
        while point1 is not None:
            print(point1.data,end=" ")
            point1 = point1.next
        print()

def main():
    dll1 = DoublyLinkedList()
    dll1.append(1)    
    dll1.append(2)    
    dll1.append(2)    
    dll1.append(1)
    print(dll1.isPalindrome())    

main()