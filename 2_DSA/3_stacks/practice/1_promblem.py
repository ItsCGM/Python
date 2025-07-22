#  Reverse a string using stack.
# i.e. "Hello" => "olleH"

s = input(str("Enter a string: "))

class Stack:
    def __init__(self):
        self.stack = []

    def push(self):
        for i in s[::-1]:
            self.stack.append(i)
            
            
    def traverse(self):
            print("Reversed string is: ", end = "")
            for i in self.stack:
                 print(i, end = "")
           


S = Stack()
S.push()
S.traverse()


# Note: In the real world, we never use stack to reverse a string.