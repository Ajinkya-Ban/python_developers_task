# 22. Find sum of even digits in a number

num = abs(int(input("ENTER A NUMBER: ")))
total = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        total += digit
    num //= 10
print("SUM OF EVEN DIGITS:", total)
