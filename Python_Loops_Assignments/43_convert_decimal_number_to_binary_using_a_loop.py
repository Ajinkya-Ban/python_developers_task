# 43. Convert decimal number to binary using a loop

num = int(input("ENTER A NON-NEGATIVE DECIMAL NUMBER: "))
if num < 0:
    print("PLEASE ENTER A NON-NEGATIVE NUMBER")
elif num == 0:
    print("BINARY: 0")
else:
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    print("BINARY:", binary)
