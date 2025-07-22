# Write a program to print the multiplication table of a given number using for loop.
print("Printing table using loops.")
num = int(input("enter the number: "))

print("Using for loop.")
for i in range(1,11):
    print(num*i)

#More tricks to solve this promblem.
for i in range(0,num*10+1,num):
    if i==0:
        continue
    print(i)

#Using while loop.
print("using while loop")
i=1
while i<=10:
    print(i*num)
    i+=1