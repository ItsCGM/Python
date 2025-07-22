#WRP to calculate the factorial of a given number using loop.
num = int(input("enter the number: "))

print("using for loop") 
fact = 1
for i in range(1,num+1):
    fact*=i
print("the factorial of given number is: ", fact)

print("using while loop.")
i=1
facto = 1
while i<=num:
    facto*=i
    i+=1
print("the factorial of the given number is: ", facto)

