a = int(input("ENTER THE FIRST NUMBER: "))
b = int(input("ENTER THE SECOND NUMBER: "))
c = int(input("ENTER THE THIRD NUMBER: "))

if(a>=b and a>=c):
    print(f"{a} is GREATEST OF ALL")
elif(b>=a and b>=c):
    print(f"{b} number is GREATEST OF ALL")
elif(c>a and c>b):
    print(f"{c} number is GREATEST OF ALL")
else:
    print("ALL ARE EQUAL")
