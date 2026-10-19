n1 = int(input("Enter the first = "))
n2 = int(input("Enter the second num = "))
res = n1 + n2
print("The addition is = ",res)
#fstring
print(f"The addition of {n1} and {n2} is {res}")

#format()
print("The addition of {} and {} is {}".format(n1,n2,res))