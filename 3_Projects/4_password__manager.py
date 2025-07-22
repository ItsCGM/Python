# Encrypting the file "passwords.txt" so non of the another person can access it.


pwd = input("What is your master password? ")


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:  # "a" is used to apend(add a data to the end of the file) new data in the existing file.
        f.write(f"{name} | {pwd} \n")

def view():
    with open("passwords.txt", 'r') as f: # "r" is use to read  data inside a file.
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print("User:", user, "| Password:", pwd)
    

while True:
    mode = input("Would you like to add a new password or vies existing ones (view, add)? and 'q' to quit. ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode")
