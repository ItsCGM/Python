# Write a class "calculator" capable of finding square, cube and square root of a number.

class number:
    def __init__(self, n):
        self.n = n
    

    def square(self):
        print(f"The square is: {self.n * self.n}")
    def cube(self):
        print(f"The cube is: {self.n * self.n * self.n}")
    def square_root(self):
        print(f"The square root is: {self.n**(1/2)}")
    @staticmethod
    def hello():
        print("Hello there!!")
a = number(25)
a.hello()
a.square()
a.cube()
a.square_root()
