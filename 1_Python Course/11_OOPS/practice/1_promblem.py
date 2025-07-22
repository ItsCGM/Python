# Create a class (2D vector) and use it to create another class representing a 3-D vector.


class D2_vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"the vector is: {self.x}i + {self.y}j")


class D3_vector(D2_vector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def show(self):
        print(f"the vector is: {self.x}i + {self.y}j + {self.z}k")


a = D2_vector(5,6)
a.show()

b = D3_vector(7,5,9)
b.show()