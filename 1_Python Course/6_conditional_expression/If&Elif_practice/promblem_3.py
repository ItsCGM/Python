# A spam comment is defined as a text containing following keywords: "make lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.
text = str(input("Enter your text message: "))
if "make lot of money" or "buy now" or "subscribe this" or "click this" or "claim your prize" in text:
    print("spams is detected in text")
else:
    print("spam is not found")
