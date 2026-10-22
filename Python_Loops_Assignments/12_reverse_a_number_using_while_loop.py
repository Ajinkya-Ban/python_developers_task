# 12. Reverse a number using while loop

num = int(input("ENTER THE NUMBER: "))
sign = -1 if num < 0 else 1
num = abs(num)
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("REVERSED NUMBER:", sign * rev)
