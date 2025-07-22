"""
a = "a very long string with emails."

emails = []
3  seconds

file is a data stored in a device. A python program can talk to the file by reading content from it and writing content to it.

types of file:
their are two type of file
1. text file (.txt, .c etc)
2. binary files (.jpg, .dat, etc)
"""

# #Opening a file.
# f = open("C:\Users\chitr\python\my_file.txt", "r")
# data = f.read()
# print(data)
# f.close()


# Writing a file.

st = "I'm a amazing guy."
f = open("my_file.txt", "w")
f.write(st)
f.close()
