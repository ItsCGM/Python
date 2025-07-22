#Creating a Queue using a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

# adding a new elements in Queue
    def Enqueue(self, data):
        new_node = Node(data)
        new_node.next = None

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        
        # current = self.head
        # while current.next:
        #     current = current.next

        # current.next = new_node
        
        #instead of traversing we use another way

        self.tail.next = new_node
        self.tail = new_node
# Traversing through the Queue
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end = "->")
            current = current.next
        print(None)

# Removing\deleting element from the Queue.
    def Dequeue(self):
        if self.head == None:
            print("Queue is empty")
            return
        
        self.head = self.head.next

        if self.head is None:
            self.tail = None  # reset the tail value if queue become empty

    def peek(self): # for accessing the iteam at the first position.
        if self.head == None:
            print("Queue is empty")

        else:
            print("elements at the 1st position is: ", self.head.data)

# size of Queue.
    def size(self):
        count = 0
        current = self.head
        while current:
            count +=1
            current = current.next
        print("Size of Queue is: ", count)



Q = Queue()
Q.Enqueue(10)
Q.Enqueue(20)
Q.Enqueue(30)
Q.traverse()
Q.size()

Q.Dequeue()
Q.peek()
Q.Dequeue()
Q.Dequeue()
Q.Dequeue()
Q.size()