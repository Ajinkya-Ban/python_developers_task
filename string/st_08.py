#isdigit()
mobile = input("Enter the mobile number = ")
if mobile == "":
    print("please enter mobile")
elif not mobile.isdigit():
    print("Invalid mobile")
elif len(mobile) != 10 and mobile[0] in "9876":
    print("Not valid")
else:
    print(mobile)