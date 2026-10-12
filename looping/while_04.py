#1234, 123 12
'''
print the reverse number using user input
'''
number = int(input("Enter the number = "))
rev = 0
while number != 0:
    digit = number % 10 # 4 3 2
    rev = rev * 10 + digit # 4320 + 1
    number = number // 10 #1
print("The reverse number = ",rev)

