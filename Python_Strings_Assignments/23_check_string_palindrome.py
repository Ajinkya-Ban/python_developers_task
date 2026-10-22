# 23. Check String Palindrome

text = input("ENTER A STRING: ")
reverse = text[::-1]

if text == reverse:
    print("IS PALINDROME")
else:
    print("NOT A PALINDROME")
