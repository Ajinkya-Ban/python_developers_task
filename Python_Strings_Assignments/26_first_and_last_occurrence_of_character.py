# 26. First And Last Occurrence Of Character

text = input("ENTER A STRING: ")
char = input("ENTER ONE CHARACTER TO FIND: ")

if len(char) != 1:
    print("PLEASE ENTER EXACTLY ONE CHARACTER")
else:
    first = text.find(char)
    last = text.rfind(char)

    if first == -1:
        print("CHARACTER NOT FOUND")
    else:
        print("FIRST OCCURRENCE:", first)
        print("LAST OCCURRENCE:", last)
