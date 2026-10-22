num = int(input("ENTER A NUMBER: "))
num = abs(num)

if num <= 9:
    print("SINGLE-DIGIT NUMBER")
elif num <= 99:
    print("DOUBLE-DIGIT NUMBER")
elif num <= 999:
    print("THREE-DIGIT NUMBER")
else:
    print("NUMBER IS OUT OF RANGE")
