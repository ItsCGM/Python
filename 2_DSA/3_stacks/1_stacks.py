# Creaating a Stack with the help of liked list.
# Stack is a linear data stricture in which the elements are inserted and deleted from one end only.
# The end from which the elements are inserted and deleted is called the top of the stack.
# In stack all the operations are performed by the head of the Linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
    

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node


    def is_empty(self):
        if self.top == None:
            print("Stack is empty")
            return
       
    def traverse(self):
        if self.is_empty():
            return
        current = self.top
        while current:
            print(current.data, end = "\n")
            current = current.next
        
    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        pop = self.top
        self.top = self.top.next
        print("Popped element is: ", pop.data)
        

S = Stack()
S.push(2)
S.push(3)
S.push(4)

S.is_empty()
S.traverse()
S.pop()
S.traverse()
S.pop()

S.traverse()
S.pop()
S.traverse()
S.pop()
