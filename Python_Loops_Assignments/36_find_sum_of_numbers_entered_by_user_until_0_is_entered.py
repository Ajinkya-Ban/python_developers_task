# 36. Find sum of numbers entered by user until 0 is entered

total = 0
while True:
    n = int(input("ENTER A NUMBER (0 TO STOP): "))
    if n == 0:
        break
    total += n
print("SUM:", total)
