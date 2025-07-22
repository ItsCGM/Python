# Creating a  stack using a list.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data) # self.stack is a list and append() is a method of list.

    def is_empty(self):
        if len(self.stack) == 0:
            print("Stack is emptu")
            
        else:
            print(f"Stack have {len(self.stack)} elements")
    
    def traverse(self):
        
        for i in self.stack:
            print(i, end = "\n")

    def pop(self):
       
            pop = self.stack.pop()
            print("Popped element is: ", pop)


S = Stack()

S.push(2)   
S.push(3)   
S.push(4)
S.push(5)
S.push(6)
S.pop()
S.is_empty()
S.traverse()
