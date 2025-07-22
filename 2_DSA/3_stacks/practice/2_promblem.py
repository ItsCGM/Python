# Undo and Redo in Text Editor.
s = input(str("Enter your string: "))
class Stack:
    def __init__(self):
        self.stack = []
        self.undo_stack = []

    def push(self):

        for i in s:
            self.stack.append(i)
        
        print(self.stack)

    def undo(self):
        if len(self.stack) == 0:
            print("Nothing to undo")
            return
        else:
            self.undo_stack.append(self.stack.pop())
            print(self.stack)
           
    def redo(self):
        redo = self.undo_stack
        if len(self.undo_stack) == 0:
            print("Nothing to redo")
            return
        else:
            self.stack.append(redo.pop())
            print(self.stack)


S = Stack()

S.push()
S.undo()
S.undo()
S.undo()
S.redo()
S.redo()
S.undo()
S.redo()
S.redo()
S.redo()
