# 13. Check whether a number is palindrome

num = int(input("ENTER THE NUMBER: "))
original = num
temp = abs(num)
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if original >= 0 and original == rev:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")
