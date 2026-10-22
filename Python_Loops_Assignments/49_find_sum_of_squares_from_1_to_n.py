# 49. Find sum of squares from 1 to n

n = int(input("ENTER A POSITIVE NUMBER: "))
if n < 1:
    print("PLEASE ENTER A POSITIVE NUMBER")
else:
    total = 0
    for i in range(1, n + 1):
        total += i * i
    print("SUM OF SQUARES:", total)
