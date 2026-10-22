# 44. Count uppercase and lowercase letters in a string

text = input("ENTER A STRING: ")
upper_count = lower_count = 0
for ch in text:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
print("UPPERCASE LETTERS:", upper_count)
print("LOWERCASE LETTERS:", lower_count)
