# 25. Extract Alphabets From String

text = input("ENTER A STRING: ")

for ch in text:
    if ch.isalpha():
        print(ch, end="")
print()
