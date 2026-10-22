# 25. Count consonants in a string

text = input("ENTER A STRING: ")
count = 0
for ch in text:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1
print("NUMBER OF CONSONANTS:", count)
