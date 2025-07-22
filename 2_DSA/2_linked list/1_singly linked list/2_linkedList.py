# Logics for adding new elements in the Linked list.

# Creating a Node class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Now creating a linked list class for the formation of the linked list.

class LinkedList:
    def __init__(self):
        self.head = None # Creating a empty Node.

# Now inserting an element in the linked list from the head
    def insert_at_head(self,data):
        new_node = Node(data) #storing the address of Node(data) in new_node  
        new_node.next = self.head
        self.head = new_node 

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
            print(current.data, end = "->")
            current = current.next
            
        print("None")

    # Inserting an element at the end of the linked list.
    def insert_at_end(self,data):
        new_node = Node(data)
        new_node.next = None
        if self.head == None:
            self.head = new_node
            return
        
        current = self.head
        while current.next: # here we use current.next because "we are finding 'None' in 'Next'."
            current = current.next
        current.next = new_node
    # Inserting an element in the middle of the linked list.
    def insert_at_mid(self, data, position): # Nth position pr insert krne ke liye hame (n-1)th position ke next me new node ki value ko insert krna padega>

        new_node = Node(data)
        # Checking the value of the Position
        if position < 0 or position > self.get_length():
            print("Plz enter the valid position")
            return
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        # using a loop to interate to the Nth position.
        current = self.head
        count = 0
    
        while current and count < (position - 1):
            current = current.next
            count += 1
        new_node.next = current.next
        current.next = new_node


        # Deleting a node 
    def delete_node(self, position):
        self.position = position

        if position < 0:
            print("Plz enter a valid Position")
            return
        
        if self.head == None:
            print("Linked list is empty")
            return
        current = self.head
        if position == 0:
            self.head = current.next
            return
        

        count = 0
        current = self.head
        while current and count < (position - 1):
            current = current.next
            count += 1

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


L = LinkedList()
L.insert_at_head(1)
L.insert_at_head(0) 
L.insert_at_end(4)
L.insert_at_end(5)
L.insert_at_end(6)
L.insert_at_mid(2,2) # 2nd position pr 2 ko insert kiya.
L.insert_at_mid(3,3)
L.insert_at_mid(-1,0)
L.insert_at_mid(9,8)
print("Printing the Linked List:")
L.traverse()
print("Length of the Linked List is: ", L.get_length())

L.find(4)
L.find(-1)
