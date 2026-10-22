# 15. Find sum of digits of a number

num = abs(int(input("ENTER THE NUMBER: ")))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("THE SUM IS:", total)
