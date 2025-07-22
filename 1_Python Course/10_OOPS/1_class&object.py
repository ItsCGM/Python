#Classes and Objects
#Class: Classes are the blue print for the creating objects.
#Objects: An Object is an instantiation of a class. When class is defined , a template(info) is defined. Memory is allocated only after object instantiation.


#Creating a class:
class Employee:
    lang = "py"     #This is a class attribute.
    salary = 120000


#crating a objects.
harry = Employee()   #This is a object attribute.
harry.name = "harry"    
print(harry.name, harry.lang, harry.salary)

rohan = Employee()
rohan.name = "rohan"
rohan.lang = "Java_Script" #Additing instant attriutes.("py" is replaced by the "java")
print(rohan.salary,rohan.name, rohan.lang, )


#Here name is object attibute and salary and lang are class attributes as they directly belong to the class.
