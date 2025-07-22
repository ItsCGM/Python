# Sets is a collection of non-repetitive,unordered elements.


# creating a set.
s = {1, 2, 3, 4, 5, 5, 5, "ram", "syam", 6.45, True} #set does not allow the duplicate elements. Its take duplicate iteams as onces.
print(s, type(s))
print(len(s))

#creating a single valued set
t1 = {1}
print(t1, type(t1))

#creating a empty set
t2 = set() # while "s2 = {}"  forms a empty set.
print(type(t2))
#Note: In sets we can't replace a exiting element by a new elements. But we can add or remove the elements from the set.



#methods in set
#add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint, issubset, issuperset, pop, remove, symmetric_difference, symmetric_difference_update, union, update



my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
my_set.add(11) #this will add the element to the set.
print(my_set)

my_set.discard(11) #this will remove the element from the set. It return nothing if the element is not present in the set.
my_set.remove(10) #this also remove element from the set but return error if the element is not present in the set.
print(my_set)

my_set.pop() #this will remove the random element from the set.
# my_set.pop(7)  #this will return error.
my_set.clear() #this will empty the set and return set().
print(my_set)

#union of two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) #this will return a new set with all the elements of both the sets.

#intersection of two sets.
print(set1.intersection(set2)) #this will return a new set with the common elements of both the sets.

set1.intersection_update(set2) #this will update the set1 with the common elements of both the sets.
print(set1) # Output, set1: {4, 5} because 4 and 5 are common in both the sets.


# set1.add(set2) #we can't add/differece elements of two sets using add/remove method.
set1.update(set2) #this will add the elements of set2 to set1.
print(set1)

#difference of two sets.
S1 = {1, 2, 3, 4, 5}
S2 = {4, 5, 6, 7, 8}
print(S1.difference(S2)) #this will return a new set with the elements of S1 which are not present in S2.
S1.intersection_update(S2) #this will update the S1 with the elements of S1 which are not present in S2.
print(S1)