class Emplopee:
    language = "Python"
    salary = 120000 
# the methods which are started from "underscore" are known as the dunder methods.


    def __init__(self, name, salary, language): #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object.")

    def getInfo(self):
        print(f"The language is {self.language} and the Salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello, welcome to the company!")
harry = Emplopee("Harry", 1300000, "Java")
# harry.name = "harry" # instead of using this we can use the __init__ function
print(harry.name, harry.salary, harry.language) #we get the reasult by the help of the instant attribute.
    