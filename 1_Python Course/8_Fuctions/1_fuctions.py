#Functions: A function is a group of statements performing a specific task.

# Syntax of a funtion.

def func1(): # defining the name of the function as "func1".
    print("hello world")


#Calling a functions
func1() #this will call the function and performs the task inside the function. 



#Printing average of three numbers.
def avg():
    a=45
    b=56
    c=46
    print("the avg of three number is: ",(a+b+c)/3)

avg() # this is known as function call. 
#if we need to find the the average 5 times so we have to just call the function 5times.

"""
types of functions
there are two types of functions
1. built in functions.(already present in python like print(), len(), range(), type()etc.)
2. user define functions.(defined by the user like we created a function above i.e. avg())
"""


print("function with arguments:")
def goodDay(name): # here "name" is called argument and the value store inside the argument is knowm as the "parameters". And a function can have more than one arguments.
    print("goodDay",name) #concatinating two strings.
goodDay("rohan")

print("function with multiple arguments:")
def student(name, age, roll):
    print("the name of student is", name)
    print("and the age is", age)
    print("having roll.no", roll)
#calling the function
student("ram",14,45)

# return value of a fuction.
def greet(name):
    gr = "hello "+ name
    return gr
a = greet("harry")
print(a) # a will contain "hello harry".


#Default Parmeter value in Functions
#default parameter is used as the default value when a value is not provided to the argument.

def goodday(name, ending="thank you"): #storing a default value\parameter to the the "ending" argument.
    print(name, ending)
goodday("rohan") #no parameter is passed to the ending.
goodday("priya", "thanks") # a new parameter is passed to the ending.

