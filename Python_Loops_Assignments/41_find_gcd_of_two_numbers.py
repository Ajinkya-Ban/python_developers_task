# 41. Find GCD of two numbers

a = abs(int(input("ENTER THE FIRST NUMBER: ")))
b = abs(int(input("ENTER THE SECOND NUMBER: ")))
while b != 0:
    a, b = b, a % b
print("GCD:", a)
