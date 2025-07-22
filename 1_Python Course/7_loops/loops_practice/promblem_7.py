#Write a program to print multiplication table of "n" using for loops in reverse order.

n = int(input("enter the number: "))

for i in range(n*10, n-1,-n):
    print(i)