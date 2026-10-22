# 14. Print Fibonacci series up to n terms

n = int(input("ENTER THE NUMBER OF TERMS: "))
a, b = 0, 1
if n <= 0:
    print("ENTER A POSITIVE NUMBER OF TERMS")
else:
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
