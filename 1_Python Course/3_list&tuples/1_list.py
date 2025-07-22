#list are the cointainer to store set of values of any data type. Lists are mutuable, can store multiple data types.
list = ["apple","ram",1,4.57,False,] #example of a list with multiple data types.
print(list)
print(type(list))


friends = ["ram","shyam","mohan","sohan","rohan",]
print(len(friends)) #length of the list

#slicing in list
print(friends[1]) #indexing in list
print(friends[-1]) #negative indexing in list
print(friends[0:4]) #slicing in list

friends.append("gohan") #append method is used to add a element at the end of the list.
print(friends)
friends.insert(4,"sunita") #insert method is used to add a new element at a specific index.
print(friends)

friends[4] = "rita" #replacing a element at a specific index. But strings are mutuable
print(friends)
friends[0:2] = ["ayushi","sakshi"] #replacing a range of elements.
#slicing in list works same as slicing in strings.


#list can be nested i.e. list inside a list.
things = ["apple","banana",[1,2,3,4],["ram","shyam","mohan"],"mango"]
print(things)

#functions in list

#append, insert, remove, pop, clear, sort, reverse, copy

fruits = ["apple","banana","mango","grapes"]

fruits.remove("banana") #remove method is used to remove a element from the list.
print(fruits)

fruits.insert(1,"pineapple") #insert method is used to add a element at a specific index.
print(fruits)
print(fruits.pop()) #pop method is used to remove the last item from the list.
print(fruits.pop(1)) #pop method is used to remove a element from a specific index.
print(fruits.clear()) #this method clear the list and returns "None".


L1 = [13,4,2,12,13,14,54,33]
print(L1)

L1.reverse() #reverse method is used to reverse the list.
print(L1)

L1.sort() #sort method is used to sort the list in ascending order.
print(L1)

#concatenation of list
L2 = [1,2,3,4]
L3 = [5,6,7,8]
print(L2+L3)
