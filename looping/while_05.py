number = int(input("Enter the number = "))
total = 0
while number != 0:
    digit = number % 10
    total += digit
    number = number // 10 
print("The reverse number = ",total)