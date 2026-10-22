# 48. Count occurrences of a character in a string

text = input("ENTER A STRING: ")
target = input("ENTER THE CHARACTER TO COUNT: ")
if len(target) != 1:
    print("PLEASE ENTER EXACTLY ONE CHARACTER")
else:
    count = 0
    for ch in text:
        if ch == target:
            count += 1
    print("OCCURRENCES:", count)
