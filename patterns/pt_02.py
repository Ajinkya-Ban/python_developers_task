row = int(input("Enter the rows = "))
for i in range(1, row+1):
    for col in range(i):
        print("*", end=" ")
    print()