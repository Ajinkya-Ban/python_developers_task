# 20. Remove Given Character

text = input("ENTER A STRING: ")
char = input("ENTER ONE CHARACTER TO REMOVE: ")

if len(char) != 1:
    print("PLEASE ENTER EXACTLY ONE CHARACTER")
else:
    print("AFTER REMOVAL:", text.replace(char, ""))
