# 24. Count vowels in a string

text = input("ENTER A STRING: ")
count = 0
for ch in text:
    if ch.lower() in "aeiou":
        count += 1
print("NUMBER OF VOWELS:", count)
