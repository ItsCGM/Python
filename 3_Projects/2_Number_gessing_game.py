import random
x = int(input("Enter the lower range: "))
y = int(input("Enter the upper range: "))
number = random.randint(x,y) # we can also use "randrange" instead of "randint" but "randrang" does't include the upper bound while "randint" inlcudes the upper bound.

guess = int(input("Ente your number: "))

i = 1
while guess != number:
    i += 1
    if guess < number:
        print("Guess a higher number")
    else: 
        print("Guess a lower number")
    
    guess = int(input("Enter your number: "))

print(f"You have guessed your number in {i} times")
