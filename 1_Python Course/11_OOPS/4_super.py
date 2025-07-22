# Super() method is used to access the parent class methods and attributes from the child class. It is used to called the parent class constructor from the child class constructor. 
# It is used to access the parent class methods and attributes from the child class.
# For example:

class Employee: 
    def __init__(self):
        print("Constructor of Employee")
    a = 1

    
class Programmer(Employee): 
    def __init__(self):
        super().__init__() # This will call the constructor of Employee class.
        # super().__init__() is used to call the constructor of the parent class.
        print("Constructor of Programmer")
    b = 2


class Manager(Programmer): 
    def __init__(self):
        super().__init__()
        # super().__init__() is used to call the constructor of the parent class.
        # This will call the constructor of Programmer class and then the constructor of Employee class.    
        print("Constructor of Manager")
    c = 3

o = Employee()
print(o.a)

print(Manager().a)