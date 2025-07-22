#Write a program to greet all the person names stored ina list, and which starts with "S".
l = ["Harry", "Soham", "Sachine", "Rahul"]
for name in l:
    if name.startswith("S"):
        print("hello",name)
        