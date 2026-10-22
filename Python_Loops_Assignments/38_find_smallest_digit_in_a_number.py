# 38. Find smallest digit in a number

num = abs(int(input("ENTER A NUMBER: ")))
smallest = 9
while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num //= 10
print("SMALLEST DIGIT:", smallest)
