from Node import Node
class Stack:
    def __init__(self) -> None:
        self.top = None

    def getTop(self):
        return self.top.data

    def push(self,val):
        newNode = Node(val)
        if  self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        if self.top is None:
            return None
        else:
            val = self.top.data
            self.top = self.top.next
        return val

    def peek(self,val):
        if self.top is None:
            return False,-1
        else:
            current = self.top
            while current is not None:
                if current.data==val:
                    return True,val
                current = current.next
        return False,-1
    
    def isPalindrome(self):
        if self.top is None:
            return False
        else:
            string = self.display_reverse()
            return string==string[::-1]

    def display(self):
        if self.top is None:
            print('Stack is empty.')
        else:
            current = self.top
            while current is not None:
                print(current.data,end=" ")
                current = current.next
            print()

    def display_reverse(self):
        string = ""
        if self.top is None:
            print('Stack is empty.')
        else:
            current = self.top
            while current is not None:
                string+=(str(current.data)[::-1])
                current = current.next
        return string
    
    def join(self,stack2):
        current = self.top
        while current.next is not None:
            current = current.next
        current.next = stack2.top

def stack_function(in_stack):
    temp_stack = Stack()
    temp_stack.push(5)
    while(in_stack.top is not None):
        temp_stack.push(in_stack.pop()*in_stack.pop())
        temp_stack.push(8)
        temp_stack.push(temp_stack.pop()+in_stack.pop())
    
    while(temp_stack.top is not None):
        in_stack.push(temp_stack.pop())
    return in_stack
in_stack = Stack()
in_stack.push(13)
in_stack.push(9)
in_stack.push(3)
in_stack.push(5)
in_stack.push(11)
in_stack.push(4)
new_stack = Stack()
new_stack = stack_function(in_stack)
new_stack.display()
in_stack.display()
in_stack