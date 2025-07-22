print("Welcome to my computer Quize")

playing = input("Do you want to Play? ")

if playing.lower() != "yes": # here the "yes" means if the user type any thing other than "yes" we quite the game.
    quit()

print("Okay!! Let's play :) ")
score = 0

answer = input("What is CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is RAM stands for? ")
if answer.lower() == "ramdom access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is PSU stands for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You have your result {score} out of 4")
