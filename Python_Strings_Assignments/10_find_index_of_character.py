# 10. Find Index Of Character

text = input("ENTER A STRING: ")
char = input("ENTER ONE CHARACTER: ")

if len(char) != 1:
    print("PLEASE ENTER EXACTLY ONE CHARACTER")
elif char in text:
    print("INDEX:", text.index(char))
else:
    print("CHARACTER NOT FOUND")
