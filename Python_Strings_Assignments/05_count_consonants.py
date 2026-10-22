# 5. Count Consonants

text = input("ENTER A STRING: ")
count = 0

for ch in text:
    if ch.isalpha() and ch not in "AEIOUaeiou":
        count = count + 1

print("NUMBER OF CONSONANTS:", count)
