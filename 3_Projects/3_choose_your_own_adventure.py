name = input("Type your name: ")
print(f"Welcome {name} to this adeventure!!")


while True:
    direction = input("You are on a dirt riad. It has come to an end and you can go left or right. Which way would you like to go? ").lower()
    
    if direction == "left":
        while True:
            river_choice = input("You come to a river. You can walk around it or swim across. Type 'walk' to walk or 'swim' to swim across: ").lower()

            if river_choice == "swim":
                print("You tried to swim but got swept by the current. You lost. \nGame Over.")
                break
            elif river_choice == "walk":
                print("You walked for many miles and safely reached the other side. \nYou Win.")
                break
            else:
                print("Not a valid option. \n'Try again.\n")
        break
    elif direction == "right":
        while True:
            mountain_choice = input("You have come to a mountain side. What do you want to do? Climb up the mountain or explore the valley? Type 'climb' or 'valley': ").lower()

            if mountain_choice == "climb":
                print("You climbed the mountain and found a beautiful view. \nYou Win!!.")
                break
            elif mountain_choice == "valley":
                print("You get lost in the valley and never returned. \nGame Over!!.")
                break
            else:
                print("Not a valid option. \nTry Again!!. \n")
        break

    else:
        print("Not a valid option. \nTry Again!!.\n")


