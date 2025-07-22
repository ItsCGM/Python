class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.next = None


    def traverse(self):
        if self.head is None:
            print("the linked list is empty")
            return
        current = self.head 
        while current is not None:
            print(current.data, end = "->")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_at_end(self, data):
        new_node = Node(data)
        new_node.next = None

        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position < 0:
            print("Ivalid Position")
            return
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
       
        current = self.head
        count = 0
        while current.next and count < (position - 1):
            current = current.next
            count += 1

        new_node.next = current.next
        current.next = new_node

        

L = LinkedList()
L.insert(10)
L.insert(20)
L.insert(30)
       
L.insert_at_beginning(5)
L.insert_at_beginning(0)
L.insert_at_end(40)
L.insert_at_position(15,3)
L.traverse()         



