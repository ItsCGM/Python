# Inheritance is the way of creating a new class from an existing class.
# The new class is called the child class or derived class and the existing class is called a parent class or base class.
# The child class inherits the properties and methods of the parent class.
# The child class can also have its own properties and methods.


# Example of inheritance:

class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent constructor called")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print("Child constructor called")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

        
# Here the child class have all the methods and properties of the parent class and also the child class have its own new methods and properties.
# The child class can also override the methods of the parent class.