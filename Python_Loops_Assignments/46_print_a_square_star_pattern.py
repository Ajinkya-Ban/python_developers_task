# 46. Print a square star pattern

n = int(input("ENTER THE SIZE OF THE SQUARE: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
