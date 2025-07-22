#Write a program to find weather a number is prime or not.
num = int(input("enter the number: "))


for i in range(2,num):
    if num%i==0:
        print("Given number is not a Prime.")
        break
else:
    print("Given number is Prime.")


#Finding the sum of n natural numbers.
print("the sum of first",num,"natural number is")

print("using 'while' loop.")
i = 0
sum =0
while i<=num:
    sum +=i
    i+=1
print(sum)

print("using 'for' looop.")
sums = 0
for i in range(1,num+1):
    sums+=i
print(sums)