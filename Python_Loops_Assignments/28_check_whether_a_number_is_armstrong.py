# 28. Check whether a number is Armstrong

n = int(input("ENTER A NUMBER: "))
if n < 0:
    print("NOT AN ARMSTRONG NUMBER")
else:
    temp = n
    total = 0
    digits = len(str(n))
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    print("ARMSTRONG NUMBER" if total == n else "NOT AN ARMSTRONG NUMBER")
