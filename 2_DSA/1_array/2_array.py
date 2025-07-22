l = [0,0,1,2,3,4,6,7,8,12,13,14,7,8]
print(len(l))

# rotating a array 
k = int(input("enter the rotation position: "))
l1 = []
l2 = []

i = 0 
while i<k:
    l1.append(l[i])
    i +=1

while k< len(l):
    l2.append(l[k])
    k += 1

l3 = l2 + l1
print(l3)
print(len(l3))

#Removing duplicates from a sort array.
# The best way to remove a dublicates from a list is to convert a list in to a set.

print(list(set(l))) # converting list to set then set to list.


# Removing all the zeros to the end.


i = 0
while i < len(l):
    if l[i]==0:
        l.remove(l[i])
    else:
      i +=1
print(l)


# Checking for a Palindrome.

list1 = [1,2,3,4,3,1]
list2 =[]

for i in list1[-1:-len(list1)-1:-1]:
    list2.append(i)
print("the list2 is:", list2)

if list1 == list2:
    print("the lists are Panidrome")
else:
    print("the lists are not Panidrome")

    