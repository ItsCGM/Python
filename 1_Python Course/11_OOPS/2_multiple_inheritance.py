# Child class can inherit the methods and properties of multiple parent classes.
# This is called multiple inheritance.

class Employee:
    company = "Google"

    def show(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Coder :
    language = "Python"
    def printLanguage(self):
        print(f"The language is {self.language}")

class Programmer(Employee, Coder): # Programmer class is inheriting from Employee and Coder classes.
    company = "YouTube"
    def showLanguage(self):
        print(f"The language is {self.name} and he is good with {self.language} languages")


a = Employee()
b = Programmer()

b.show("John", 100000)
b.printLanguage()
b.showLanguage()
