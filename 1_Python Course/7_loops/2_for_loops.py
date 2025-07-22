# Creating a for loop. Printing numbers with the help of for loop.
for i in range(6): # Here range includes the numbers from 0 to 5 and 6 is excluded.
    print(i)


# for loop is used to iterate through a sequence like list, tuple, or string.[iterables]

# Step size in for loop.
print("Printing step size in loop.")
for i in range(0,10,2): # here the (2) is step size of the loop.
    print(i)

#Printing the elements of a list using for loop.
print("Iterating the elements of list using for loop")

l = [12,32,22,15,31,54]
for i in l:
    print(i)

# We can also iterate the elements of tuple, string, set, dic using for loop.

print("Iterating over strings")
s = "Mohan"
for i in s:
    print(i)

# An optional else can be used with a for loop if the code is to be executed when the looops exhausts.

t = ("ram", "syam")
for i in t:
    print(i)
else:
    print("Done")

#Both the for and while loop are alike.

# Breake, Continue and Pass 
print("using break")
for i in range(10):
    if i==3:
        break # break stands for, "exiting the loop".
    print(i)
print("using continue")   
for i in range(10):
    if i==3:
        continue # Skip the iteration.
    print(i)

print("using pass")
for i in range(65):
    pass  #pass key word is used to skip the whole loop. 
     