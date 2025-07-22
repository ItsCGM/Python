name = "chitragupt maurya" #this is a string

#NOTE: strings are immutable i.e. we can't change the value of a string
#slicing a string
print(len(name)) #length of string
print(name[2]) #slicing by indexing
print(name[0:5])#slicing by range
print(name[0:5:2]) #slicing by range and step
print(name[0:]) 
print(name[:10])


#we can also perform negative slicing
print(name[-4:-1])


#NOTE: in positive slicing the counting starts from 0 while in negative slicing the counting starts from -1.

#functions in strings
print(len(name))
print(name.lower())
print(name.upper())
print(name.replace("chitragupt","jhule"))

print(name.find("t")) #print the index of occurance

print(name.capitalize()) #capitalize the first letter of first word of the string

print(name.startswith("chitr"))
print(name.endswith("urya"))          