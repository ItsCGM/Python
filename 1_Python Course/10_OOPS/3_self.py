class Employee:
    language = "Python"  
    salary = 120000

    def getInfo(self): # self is a reference to the current instance of the class
        print(f"The language is {self.language} and the Salary is {self.salary}")
    
    @staticmethod # this is a static method and can be called without creating an instance of the class.
    # static methods are used when we do not need to access the instance or class attributes.
    def greet():
        print("Hello, welcome to the company!")

rohan = Employee() 
rohan.language = "JavaScript" 
rohan.greet()# calling the greet method
rohan.getInfo() # this can be also written as Employee.getInfo(rohan)
