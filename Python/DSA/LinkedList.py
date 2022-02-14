from Node import Node
from MergeLL import mergeList
class LinkedList:
    '''Linked List class have following functions for Linked List:
    1.Append
    2.Pop
    3.Lookup
    4.SortList
    5.Palindrome Checker
    6.Reverse Linked List
    7.Simple Merge(Unsorted)
    8.Merge(Sorted)
    9.Get Head
    10.Get Middle
    11.Get Tail
    12.Display
    '''
    def __init__(self)->None:
        '''Initialize new Linked List'''
        self.head = None
    
    def append(self,val,pos=None):
        '''Add a new element in Linked List'''
        newNode = Node(val)
        point1 = self.head
        #if linked list is empty
        if self.head is None:
            self.head = newNode
        #insertion at head position
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

    def pop(self,pos=None,val=None):
        point1 = self.head
        global_pos = 0
        if pos==0:
            self.head = self.head.next
        elif val is not None:
            point2 = Node()
            while point1.next is not None:
                if point1.data == val:
                    point2.next = point1.next
                    return
                point2 =  point1
                point1 = point1.next
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
        point1 = self.head
        while point1.next is not None:
            point1 = point1.next
        return point1
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

    def reverseList(self):
        current = self.head
        previous = None
        while current is not None:
            forward = current.next
            current.next = previous
            previous = current
            current  = forward
        self.head = previous

    def isPalindrome(self):
        current = self.head
        values1 = ""
        while current is not None:
            values1+=str(current.data)
            current = current.next
        self.reverseList()
        current = self.head
        values2 = ""
        while current is not None:
            values2+=str(current.data)
            current = current.next
        self.reverseList()
        return values1==values2
    
    def simpleMerge(self,ll2):
        ll3 = LinkedList()
        selfLLHead = self.head
        secondLLHead = ll2.head
        while selfLLHead is not None:
            ll3.append(selfLLHead.data)
            selfLLHead = selfLLHead.next
        while secondLLHead is not None:
            ll3.append(secondLLHead.data)
            secondLLHead = secondLLHead.next
        return ll3

    def merge(self,ll2):
        ll3 = LinkedList()
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

    def removeDuplicatesInSortedLL(self):
        current = self.head
        while current.next is not None:
            if current.data == current.next.data:
                self.pop(None,current.data)
            current = current.next
    def traverse(self) -> None:
        point1 = self.head
        while point1 is not None:
            print(point1.data,end=" ")
            point1 = point1.next
        print()

def main():
    ll1 = LinkedList()
    items = []
    for i in range(1,11): items.append(ri(1,11))
    items.sort()
    print(items)
    for i in items:
        ll1.append(i)
    ll1.removeDuplicatesInSortedLL()
    #ll1.pop(None,2)
    ll1.traverse()
    #ll1.pop(None,5)
    #ll1.traverse()
from random import randint as ri
main()
