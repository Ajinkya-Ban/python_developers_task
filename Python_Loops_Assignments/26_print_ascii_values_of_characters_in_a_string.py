# 26. Print ASCII values of characters in a string

text = input("ENTER A STRING: ")
for ch in text:
    print(ch, "=", ord(ch))
