
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
N1 = Node(10)
N2 = Node(20)
N3 = Node(30)
N4 = Node(40)

N1.next = N2
N2.next = N3
N3.next = N4

print(N1.next)
print(N2)
#here N1.next and N2 cointains the same location in the memory


# Now traversing ove the Node.
current = N1
while current != None:
    print(current.data, end = "->")
    current = current.next
print(None)

