# 7. Calculate factorial of a number using for loop

n = int(input("ENTER THE NUMBER: "))
if n < 0:
    print("FACTORIAL IS NOT DEFINED FOR NEGATIVE NUMBERS")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("FACTORIAL IS:", fact)
