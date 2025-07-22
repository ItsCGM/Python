# A Queue is a linear data structure that follows the "first in and first out" principle.
# e.g. people standing at in a line(queue) at a ticket counter.


# In a Queue, a new elemet is added from the end(rear) and a element is deleted from the front.

# Creating a simple Queue using list.

Queue = []

# adding elements
Queue.append(10)
Queue.append(20)
Queue.append(30)
print("Adding element in a Queue: ", Queue)


# removing elements from the Queue.
Queue.pop(0) # removing\deleting element of the '0'th index.

print("Removing element from the Queue: ", Queue)
