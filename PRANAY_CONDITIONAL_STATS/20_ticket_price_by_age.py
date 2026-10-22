n = int(input("Enter your age: "))

if(n<=5):
    print("YOUR TICKET IS FREE")
elif(n<18):
    print("YOUR TICKET IS 50 RUPEES")
elif(n<60):
    print("YOUR TICKET IS 100 RUPEES")
else:
    print("YOUR TICKET IS FREE")
