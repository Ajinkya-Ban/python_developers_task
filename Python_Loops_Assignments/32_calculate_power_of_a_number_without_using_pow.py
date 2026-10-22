# 32. Calculate power of a number without using pow

base = int(input("ENTER THE BASE: "))
power = int(input("ENTER THE POWER (NON-NEGATIVE): "))
if power < 0:
    print("PLEASE ENTER A NON-NEGATIVE POWER")
else:
    result = 1
    i = 1
    while i <= power:
        result *= base
        i += 1
    print("RESULT:", result)
