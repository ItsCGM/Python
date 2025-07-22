# 3. Can we have a set with 18(int) and "18"(str) as a value in it.
s = {18, "18"}
print(s)
print(len(s)) # we get the length of the set as 2 because both the elements are different.

# 4. What will be the lenght of the given set:
s = {20, "20", 20.0}
print(s, len(s)) #the output is True, because in python "1==1.0"
