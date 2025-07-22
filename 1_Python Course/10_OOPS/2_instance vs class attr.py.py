class Employee:
   language = "Python"  # This is an Class attribute
   salary = 120000

rohan = Employee() #This is an Object Attribute.
rohan.language = "JavaScript" #This is an instance attribute
print(rohan.language, rohan.salary)

#The instance attribute takes preference over the class attribute.