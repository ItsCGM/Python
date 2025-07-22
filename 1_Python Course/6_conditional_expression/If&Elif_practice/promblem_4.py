#write a program to calculate the grade of a student from his marks from the following scheme:


marks = int(input("Enter your obtained marks: "))
if marks>=90 and marks<=100:
    print("excellece")
elif marks>=80 and marks<90:
    print("You obtained grade A")
elif marks>=70 and marks<80:
    print("You obtained grade B")
elif marks>=60 and marks<70:
    print("You obtained grade C")
elif marks>=50 and marks<60:
    print("You obtained grade D")
else: 
    print("You obtained grade F")