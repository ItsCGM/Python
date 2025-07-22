# keys/slots   values/data

# Linear Probing

class Dictionary:
    def __init__(self, size):
        self.size = size
        self.key = [None] * self.size    # here we are creating two arrays one for keys and another for the val".
        self.value = [None] * self.size
    
    

    def hash_function(self, key):
        
        return abs(hash(key)) % self.size   # abs and hash are in-built function of the python where "Hash" calculate the hash value while "abs" covert the hash value into positive value if it is -ve.
    

    def insert(self, key, value): # etane bade wale code se achha ek aur code 3_hashing me
        hash_value = self.hash_function(key)

        if self.key[hash_value] is None:
            self.key[hash_value] = key
            self.value[hash_value] = value

        else:
            if self.key[hash_value] == key:  
                self.value[hash_value] = value
            
            else:
                current = (hash_value + 1) % self.size
                while current != hash_value:
                    if self.key[current] is None or self.key[current] == key:
                        self.key[current] = key
                        self.value[current] = value
                        return
                    current = (current + 1) % self.size
                print(f"Hash table is full cann't insert {key}")

    def display(self):
            for i in range(self.size):
                print(f"Slot {i}: {self.key[i]} => {self.value[i]}")
    

d = Dictionary(5)
d.insert("apple", 100)
d.insert("banana", 200)
d.insert("grapes", 300)
d.insert("orange", 400)
d.insert("mango", 500)


d.display()