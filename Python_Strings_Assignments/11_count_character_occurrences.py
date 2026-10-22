# 11. Count Character Occurrences

text = input("ENTER A STRING: ")
char = input("ENTER ONE CHARACTER: ")

if len(char) != 1:
    print("PLEASE ENTER EXACTLY ONE CHARACTER")
else:
    count = 0
    for ch in text:
        if ch == char:
            count = count + 1
    print("OCCURRENCES:", count)
