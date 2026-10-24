#rows = int(input("Enter the rows = "))
# for i in range(1,rows+1):
#     for cols in range(1, i + 1):
#         print(cols, end=" ")
#     print()

rows = int(input("Enter the rows = "))
for i in range(1,rows+1):
    for cols in range(1, i + 1):
        print(i, end=" ")
    print()