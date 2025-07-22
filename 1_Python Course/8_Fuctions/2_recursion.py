#Recursion is a function which calls itself.
''' 
1! = 1
2! = 2 x 1
3! = 3 x 2 x 1
4! = 4 x 3 x 2 x 1

in simple way we can say

n! = n x (n-1)!
'''
#finding the factorial of a number.
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
n=int(input("enter the value of n: "))
print("finding the factorial of a number using recursion")
print(factorial(n))

print("finding the fatorial of a number using while loop.")
i = 1
p=1
while i<=n:
    p *= i
    i+=1
print(p)


