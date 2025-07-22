a = [2,6,5,7,11,12,14,9,14]

a.sort() # sort() function ka use array ko accending order me karne ke liye kiya jata h.

print(a[-1]) #Finding the largest element in the array.
print(a[0]) # Findind the smallest elements in the array.

# for finding the maximum and minimum element of the array we can use the build in function "max and min".

print("the largest element is: ", max(a))
print("the minimum element of the array is: ", min(a))


# Reversing a array.
l =[]
i = -1
while i>= -(len(a)):
    m = a[i]
    l.append(m)
    i -= 1

print("reversing an array:\n",l)


# Finding the sum of all element in a array.

print("the sum of all element of array is:", sum(a)) # for finding the sum of a array we have a built in function "sum".

# finding an element in a array.
if 15 in a:
    print(True)
else:
    print(False)

