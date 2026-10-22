# 39. Count total words in a string

text = input("ENTER A STRING: ")
count = 0
for word in text.split():
    count += 1
print("NUMBER OF WORDS:", count)
