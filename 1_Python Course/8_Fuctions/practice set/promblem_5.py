'''Write a python function to print first n lines of the following pattern: 
*** 
**               
*  for n = 3 '''
n = int(input("enter the number: "))

print("using recursion.")
def pattern(n):
    if n==0:

        return
    print("*"*n)
    pattern(n-1)
pattern(n)

print("using while loop")
i=n
while i>0:
    print(i*"*")
    i-=1


print("using for loop")

for i in range(n,0,-1):
    print(i*"*")

