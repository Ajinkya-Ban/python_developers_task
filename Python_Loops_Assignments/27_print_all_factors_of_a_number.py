# 27. Print all factors of a number

num = int(input("ENTER A POSITIVE NUMBER: "))
if num <= 0:
    print("PLEASE ENTER A POSITIVE NUMBER")
else:
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
