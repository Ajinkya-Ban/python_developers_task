# 18. Print prime numbers between 1 and 50

for num in range(2, 51):
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)
