# 4. Count Vowels

text = input("ENTER A STRING: ")
count = 0

for ch in text:
    if ch in "AEIOUaeiou":
        count = count + 1

print("NUMBER OF VOWELS:", count)
