from colorama import Fore, Back, Style ,init

number = int(input("Enter the number = "))
total = 0
while number != 0:
    digit = number % 10
    if digit % 2 ==0:
        total += digit
    number = number // 10 
print(Fore.RED + Back.WHITE +"The addition even number is = ",total,Style.RESET_ALL)