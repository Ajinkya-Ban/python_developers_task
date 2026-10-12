'''
print 1 to 10 number using for loop
'''
start_val = int(input("Enter the starting value = ")) #1
end_val = int(input("Enter the ending value = "))
for i in range(start_val,end_val):
    if i % 2 == 0:
        print(i)