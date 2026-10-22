# 47. Calculate the average of n numbers

n = int(input("HOW MANY NUMBERS WILL YOU ENTER?: "))
if n <= 0:
    print("PLEASE ENTER A POSITIVE COUNT")
else:
    total = 0
    for i in range(n):
        total += float(input("ENTER A NUMBER: "))
    print("AVERAGE:", total / n)
