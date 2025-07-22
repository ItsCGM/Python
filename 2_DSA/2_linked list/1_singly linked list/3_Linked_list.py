# Deleting a node in a Linked List.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # entering a element inside a list.
    def insert(self, data):
        new_node = Node(data)
        new_node.next = None
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def remove(self, data):
        if self.head == None:
            print("Linked list is empty")
            return
        
         # self.head also stores the address of the first Node.
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next # if current.next.data is not == data then move to the next node.
        print("f{data} is not found.")

    def traverse(self):
        current = self.head
        while current.next:
            print(current.data, end = "->")
            current = current.next
        print("None")
            
L = LinkedList()

L.insert(2)
L.insert(3)
L.insert(4)
L.insert(5)
L.traverse()
L.remove(3)
L.traverse()