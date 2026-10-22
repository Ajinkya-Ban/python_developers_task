# 42. Find LCM of two numbers

a = abs(int(input("ENTER THE FIRST NUMBER: ")))
b = abs(int(input("ENTER THE SECOND NUMBER: ")))
if a == 0 or b == 0:
    print("LCM: 0")
else:
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    print("LCM:", (a * b) // x)
