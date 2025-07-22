# WRP to find a post is talking about "Chitragupt"

post = "chitragupt is a good boy, chitragupt is very good, chitragupt is great"

if "Chitragupt" in post:
    print("the post is about chitragupt") 
else:
    print("the post is not about chitragupt")


#important trick
if "Chitragupt".lower() in post.lower():  # coverting post and chitragupt to the lower case to be both alike.
    print("the post is about chitragupt")
else:
    print("the post is not about the chitragupt")
  