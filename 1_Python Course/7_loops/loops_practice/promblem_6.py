#Write a program to print the following star pattern. 
"""
* * * 
*   *   for n = 3 
* * *
"""
n = int(input("enter the number: "))

i=1
while i<=n:
    if i==1 or i==n:
        print(n*"* ")
    else:
        print("*",(n)*" ", " *")
    i+=1
