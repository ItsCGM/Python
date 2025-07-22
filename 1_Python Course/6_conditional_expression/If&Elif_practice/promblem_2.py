#Write a program to find out whether a student has passed or failed if it required a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

mm =int(input("enter the maximum marks: "))
m = int(input("enter your maths marks: "))*100/mm
s = int(input("Enter your science marks: "))*100/mm
e = int(input("Enter your english marks: "))*100/mm

print(m,"% you got in maths")
print(s,"% you got in science")
print(e,"% you got in english")
print((m+s+e)/3,"% you got of total")
if m<33 or s<33 or e<33:
    print("failed")
elif ((m+s+e)/3)<40:
    print("failed")
else: 
    print("congrantulation your are passed")