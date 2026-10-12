from colorama import Fore,Back, Style,init 
init()
start_val = int(input("Enter the starting value = ")) #1
end_val = int(input("Enter the ending value = "))
total = 0
for i in range(start_val,end_val):
    total = total + i
print(Fore.GREEN+"The addition is = ", total)
