# 1. Write a python to fill in a letter template given below with name and date.

letter = '''
        Dear <|NAME|>,
        You are selected!
        <|Date|>'''
print(letter.replace("<|NAME|>","Chitragupt Maurya").replace("<|Date|>","12-12-2021")) 

# 2.Write a program to detect double space in a string.
name = "chitragupt maurya is a good  boy"
print(name.find("  "))

# 3.if occurance is not found in the string then it return -1 as result.
print(name.find("xyz"))

# 4. Write a python program to replace double spaces with single spaces.
print(name.replace("  "," "))

# printing a list with the help of escape sequence character.
letter = "Dear Chitragupt,\n\tYou are selected!\n\t12-12-2021"
print(letter)