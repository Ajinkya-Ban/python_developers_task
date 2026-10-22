# 24. Extract Digits From String

text = input("ENTER A STRING WITH DIGITS: ")

for ch in text:
    if ch.isdigit():
        print(ch, end="")
print()
