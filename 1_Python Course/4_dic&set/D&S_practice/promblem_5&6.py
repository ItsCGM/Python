# 5. s={}, What type of s is??
s = {}
print(type(s))


# 6. Create an empty dictionary. allow  4 friends to enter their favorite language as value and use key as their names. Assumes that the names are unique.

name1 = input("ente the name: ")
language1 = input("enter the favorite language: ")
s.update({name1:language1})
name2 = input("ente the name: ")
language2 = input("enter the favorite language: ")
s.update({name2:language2})
name3 = input("ente the name: ")
language3 = input("enter the favorite language: ")
s.update({name3:language3})
name4 = input("ente the name: ")
language4 = input("enter the favorite language: ")
s.update({name4:language4})
print(s)

# When two friends got the same name then the value of the first friend will get updated by the second value.
#Because in dictionary unique "key" is allowed but "value" may be double or two keys may have the same "value". And a "key" can hold more than one "values".
