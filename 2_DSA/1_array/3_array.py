# Finding the missing number in a array from 1 to n.

l1 = [1,2,3,4,5,6,7,8,9,10,12,13,14]
l2 = []
i = 1
while i<=15:
    l2.append(i)
    i += 1
print(l2)

print(list(set(l2)-set(l1)))

# We can also append number 1 to n in a set using set(range(1, n+1))

l3 = list(set(range(1,5)))
print(l3)


# Merging two arrays
# we can simply add two array using "+".
print(l2+l3)



#finding intersection of two arrays.
s2 = set(l2)
s3 = set(l3)

s_final = list(s2.intersection(s3))
print(s_final)

