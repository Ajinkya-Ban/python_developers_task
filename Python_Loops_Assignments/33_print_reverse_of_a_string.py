# 33. Print reverse of a string

text = input("ENTER A STRING: ")
reverse = ""
for ch in text:
    reverse = ch + reverse
print(reverse)
