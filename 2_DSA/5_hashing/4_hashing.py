# Chaining



class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Now creating a linked list class for the formation of the linked list.

class LL:
    def __init__(self):
        self.head = None # Creating a empty Node.


    def get_length(self):
        length = 0
        current = self.head 
        while current:
            length +=1
            current = current.next
        return length
    
    # Traversing over the Linked List(or printing the elements of the Liked List.)
    def traverse(self):
        current = self.head
    
        while current: #"while current != None" both refer to the same output.
            print(f"{current.key} --> {current.value} ")
            current = current.next    
        print("None")

    # Inserting an element at the end of the linked list.
    def insert_at_end(self,key, value):
        new_node = Node(key, value)
        new_node.next = None
        if self.head == None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Removing a key from linked list.
    def remove(self, key):
        if self.head is None:
            print("The Linked List is emptY")
            return
        

        if self.head.key == key:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
        print("f{key} is not found inside the Linked List.")

    def find(self, data):
        if self.head.data == data:
            print(f"{data} is founda at position: 0")
            return
        current = self.head
        count = 1
        while current.next:
            if current.next.data == data:
                print(f"{data} is found at position: {count}")
                return
            count +=1
            current = current.next
        print(f"{data} is not found in linked list.")



class Dictionary:
    def __init__(self, capacity):

        self.capacity = capacity
        self.size = 0

        
        # Create a array of LL
        self.buckets = self.make_array(self.capacity)

    def make_array(self, capacity):
        L = []
        for i in range (capacity):
            L.append(LL())
        return L

    def put(self, key, value):
        pass
    

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity
    