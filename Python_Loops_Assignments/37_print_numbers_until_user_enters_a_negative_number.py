# 37. Print numbers until user enters a negative number

while True:
    n = int(input("ENTER A NUMBER (NEGATIVE TO STOP): "))
    if n < 0:
        break
    print(n)
