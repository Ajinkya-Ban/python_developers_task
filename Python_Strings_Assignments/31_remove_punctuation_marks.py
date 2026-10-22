# 31. Remove Punctuation Marks

import string

text = input("ENTER A STRING: ")
result = ""

for ch in text:
    if ch not in string.punctuation:
        result = result + ch

print("WITHOUT PUNCTUATION:", result)
