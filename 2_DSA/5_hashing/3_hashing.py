# Linear Probing

class Hash_Table:
    def __init__(self, size):
        self.size = size
        self.key = [None] * self.size    # here we are creating two arrays one for keys and another for the val".
        self.value = [None] * self.size
    
    

    def hash_function(self, key):
        
        return abs(hash(key)) % self.size   # abs and hash are in-built function of the python where "Hash" calculate the hash value while "abs" covert the hash value into positive value if it is -ve.
    

    def insert(self, key, value):
        hash_value = self.hash_function(key)

        current = hash_value

        # Loop to handel linear probing when collision occurs.
        while self.key[current] is not None and self.key[current] != key:
            current = (current + 1) % self.size
            if current == hash_value:
                print(f'Hash Table is full can not insert "{key}"')
                return
        
        self.key[current] = key
        self.value[current] = value
    

    def display(self):
        for i in range(self.size):
            print(f"Slot {i}: key = {self.key[i]}, value = {self.value[i]}")

    def search(self, key):
        current = 0
        while self.key[current] !=key:
            current += 1
            if current == self.size:
                print(f"{key} is not found inside the hash table")
                return
        print(f"Slot {current} {self.key[current]}: {self.value[current]}")

    def replace(self, slot, key, value):
        self.key[slot] = key
        self.value[slot] = value


# Create an instance of the Dictionary with size 5
H = Hash_Table(5)

# Inserting values
H.insert("apple", 100)
H.insert("banana", 200)
H.insert("grapes", 300)
H.insert("orange", 400)
H.insert((1,3), 500)
# Display the hash table
H.display()

#printing iteams if present inside the "hash_table".
H.search("apple")
H.search("iwi")


#Replacing items

H.replace(2, "Kiwi", 600)
H.search("Kiwi")

