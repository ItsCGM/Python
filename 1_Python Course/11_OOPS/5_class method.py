# A class method is a method thet is bound to the class and not the instance of the class. It can modify class state that applies across all instances of the class.
# for example

class Employee:
    a = 1 
    def show(self):
        print(f"The class attribute of a is {self.a}")

e = Employee()
e.a = 45
e.show() # The class attribute of a is 4. But when we use class method


class Employee:
    a = 1 
    @classmethod
    def show(cls): # in  class method we use "cls" instead of "self". 
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45
e.show() # The class attribute of a is 1. But when we use class method
