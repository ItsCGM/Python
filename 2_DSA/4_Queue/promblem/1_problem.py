# Creating Queue with the help of two Stacks.

# In this case we create two Stacks, one stack is for "enqueue" and another stack for "dequeue"

# creating a stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.de_stack = None
        self.en_stack = None

    def en_queue(self, value):
        new_node = Node(value)
        new_node.next = None

        if self.de_stack is None:
            self.de_stack = new_node
            return
        
        current = self.de_stack
        while current.next:
            current = current.next
        current.next = new_node
        


    