#Create a Class "Programmer" for storing information of few programmers working at Microsoft. 

class Programmer:
    company = "Microsoft"

    def __init__(self, name, id_no, salary, pin):
        self.name = name
        self.id_no = id_no
        self.salary = salary
        self.pin = pin
    

c = Programmer("Ranu", 1200000, 45326, 275202)
print(c.name, c.id_no, c.salary, c.pin)


v = Programmer("Vijay", 1120000, 455866, 275252)
print(v.name, v.id_no, v.salary, v.pin)
