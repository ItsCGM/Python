#Creating a Dictionary, dictonary store the data in the form of key-value pair.
marks = {
    "m1": 45,
    "m2": 56,
    "m3": 78,
    "m4": 86,
    "m5": 90,
    "m6": 100
}
print(marks,type(marks))
print(len(marks))

d ={} #creating a empty dictionary.

#dict are unordered, means the order of the elements in the dictionary is not fixed.
# dict can be also created in nested form.


#Accessing the elements of a dictionary
#Accessing the elements of a dictionary is done by using the key of the element.  
  
print(marks["m1"]) #Return error  if the key is not presint in the dictionary.
print(marks.get("m1")) #print None if the key is not present in the dictionary.
#both the methods are used to access the elements of a dictionary.


#Methods in dictionary
#clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update, values
print("printing the keys, values, and iteams of a dict")
print(marks.keys(), type(marks.keys())) #keys[m1, m2, m3... m6]
print(marks.values()) #values [45, 56, 78,....100]
print(marks.items()) #this will return the key-value pair in the form of tuple.


#updating the dictionary
print("updating the dic")
marks["m1"] = 50 # updating the new value
marks.update({"m1": 60}) # this also update the key value.
marks.update({"m7": 60}) #adds a new key-value pair to the dictionary.
#both the methods are used to update the dictionary.

print(marks)


#Removing items from the dictionary.
#pop, popitem, clear

marks.pop("m1") #this will remove the key-value pair from the dictionary.
# marks.pop() in dictionary returns error.
print(marks)

marks.popitem() #this will remove the last key-value pair from the dictionary.
print(marks)

marks.clear() #this will clear the dictionary.
print(marks)
