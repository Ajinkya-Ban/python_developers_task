# 40. Check whether a number is a perfect number

num = int(input("ENTER A POSITIVE NUMBER: "))
total = 0
if num > 1:
    for i in range(1, num):
        if num % i == 0:
            total += i
print("PERFECT NUMBER" if num > 0 and total == num else "NOT A PERFECT NUMBER")
