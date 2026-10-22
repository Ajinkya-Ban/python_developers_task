# 36. Remove Duplicate Characters

text = input("ENTER A STRING: ")
result = ""

for ch in text:
    if ch not in result:
        result = result + ch

print("WITHOUT DUPLICATES:", result)
