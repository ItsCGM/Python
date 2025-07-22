l = [None] * 2

def hash_value(a):
    return a % 2


def insert(a):
    index = hash_value(a)
    if l[index] == None:
        l[index] = a
    else:
        i = (index + 1) % 2
        while i != index:
            if l[i] is None:
                l[i] = a
                return
            i = (i + 1) % 2
            print(f"Hash table is full cann't insert {a}")

insert(89)
insert(89)
insert(89)

print(l)

# Note: In hashing we find out the "hash value" of "key".