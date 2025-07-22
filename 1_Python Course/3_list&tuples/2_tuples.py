#tuples are as similar as lists but tuples are immutable i.e. we can't change the value of a tuple
#tuples are faster than lists


#creating a tuple: tuples are created inside a () brackets.

t = (1,2,3,"rohan",False,1.3) #example of a tuple with multiple data types.
print(type(t))
print(len(t)) #length of the tuple

#creating a single value tuples
t1 = (1)
print(type(t1))

t2 = (1,) # single values tuple are created using "," inside the bracket
print(type(t2))


#tuples method

my_tup = (45,334,32,45,64,34,35,32,23)
print(my_tup.count(45)) #this is used to count number of occurance of a element in a tuple.
print(my_tup.index(64)) #this is used to find the index of a element in a tuple.


#finding a element in a tuple
print(45 in my_tup) 
print(66 in my_tup)


#slicing in tuples

print(my_tup[0:5]) 
print(my_tup[0:5:2]) #slicing with step
#concatination of tuples

t3 = (1,2,3,4)
t4 = (5,6,7,8)
t5 = t3+t4


print(t5) #this will print the concatenated tuple.
t6 = t3*3
print(t6) #this will print the tuple 3 times.


#unpacking of tuples
a,b,c,d = t3
print(a) #this will print the value of a
print(a,b,c,d)