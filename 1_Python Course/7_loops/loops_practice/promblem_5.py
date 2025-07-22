#WRT a program to print following pattern

"""
  *
 ***
******
for the value of n=3"""


n = int(input("enter your number: "))

print("using while loop.")
i=1
while i<=n:
    print((n-i)*" ",((2*i)-1)*"*")
    i+=1


print("Using for loop.")

for i in range(1,n+1):
    print((n-i)*" ",((2*i)-1)*"*")

    