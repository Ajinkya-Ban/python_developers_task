# 45. Remove spaces from a string using a loop

text = input("ENTER A STRING: ")
result = ""
for ch in text:
    if ch != " ":
        result += ch
print("STRING WITHOUT SPACES:", result)
