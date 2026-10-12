'''
The program for sum of even numbers between start_val and end_val
'''
start_val = int(input("Enter the starting value = ")) #1
end_val = int(input("Enter the ending value = ")) # 10
total=0
i = start_val
while i <= end_val:
    if i % 2 == 0:
        total = total + i # 6
    i += 1
print("The final sum = ", total)



