# Celelbrity Promblem: Its means that there is a person who is known by everyone but he doesn't know anyone.
# M[i][j] = 1 means "i"th person known "j"th person for M[i][j] = 0 means "i"th person does't know "j"th person.
# However here M[i][i] or M[j][j] is equal to zero.



arr = [[0, 1, 0],
       [0, 0, 0],
       [1, 1, 0]]

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, arr):
        
        for i in range(len(arr)):
            self.stack.append(i)
    
    def checking_cele(self):
        while len(self.stack) >= 2:
            i = self.stack.pop()
            j = self.stack.pop()
            if arr[i][j] == 0: # here i does't know j, i.e. j is not a celebrity.
                self.stack.append(i)
            else: 
                self.stack.append(j)  # if i know j then j may be a celebrity.

        celeb = self.stack.pop() # checking the left one is really a celebrinty or not.
        for i in range(len(arr[celeb])):
            if i != celeb:
                
                if arr[i][celeb]==0 or arr[celeb][i]==1:
                    print("No body is celebrity")
                    return
                else:
                    print(f"{celeb} index person is celebrity")

    def traverse(self):
        
        for i in self.stack:
            print(i)


S = Stack()
S.push(arr)
S.checking_cele()
S.traverse()
    


