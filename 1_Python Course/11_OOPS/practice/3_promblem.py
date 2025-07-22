# Create a class "Employee" and add salary and increment properties to it.


class Employee:
    def __init__(self, salary, increment=7.0):
        self.salary = salary
        self.increment = increment
        
        def apply_increment(self):
            self.salary = self.salary + (self.salary * self.increment) / 100
            return self.salary


a = Employee(10000)
print(a.salary)
a.apply_increment()
print(a.salary)