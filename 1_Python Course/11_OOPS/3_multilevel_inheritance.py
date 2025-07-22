# When a child class become a parent for the another child class, it is called multilevel inheritance.
# For exmple:

class Employee:
    company = "Google"

    def show(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Coder(Employee): # Coder class is inheriting from Employee class.
    language = "Python"
    def printLanguage(self):
        print(f"The language is {self.language}")

class Programmer(Coder): # Programmer class is inheriting from Coder class and indirectly from the Employee class.
    company = "YouTube"
    def showLanguage(self):
        print(f"The language is {self.name} and he is good with {self.language} languages")

# Coder class become a parent for the Programmer class. This is known as the Multilevel Inheritance.

a = Programmer()
a.show("mohan", 12000)
a.printLanguage()
a.showLanguage()