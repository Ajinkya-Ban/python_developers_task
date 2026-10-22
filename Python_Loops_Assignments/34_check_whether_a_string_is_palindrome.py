# 34. Check whether a string is palindrome

text = input("ENTER A STRING: ")
reverse = ""
for ch in text:
    reverse = ch + reverse
print("PALINDROME" if text == reverse else "NOT A PALINDROME")
