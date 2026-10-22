# 19. Check whether a number is prime

num = int(input("ENTER A NUMBER: "))
prime = num > 1
if prime:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
print("PRIME NUMBER" if prime else "NOT A PRIME NUMBER")
