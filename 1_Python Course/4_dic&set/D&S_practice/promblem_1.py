# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
dictionary = {
    "Namaste": "Hello",
    "Dhanyavaad": "Thank you",
    "Paani": "Water",
    "Kitaab": "Book",
    "Mitra": "Friend",
    "Ghar": "Home",
    "Pyaar": "Love",
    "Khushi": "Happiness",
    "Sooraj": "Sun",
    "Chaand": "Moon"
}
x = input("Enter your Hindi word: ")
print("The English translation of your word is: ", dictionary.get(x)) # here we will not use hienglish_to_english[x] because if the key is not present in the dictionary then it will return error.
