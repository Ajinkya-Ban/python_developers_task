row = int(input("Enter the rows = "))
for i in range(row, 0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
# for i in range(1, row+1):
#     for col in range(i):
#         print("*", end=" ")
#     print()
# for i in range(row, 0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()