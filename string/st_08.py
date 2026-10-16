
# isdigit()

mobile = input("Enter the mobile number = ")

if mobile == "":
    print("Please enter mobile number")

elif not mobile.isdigit():
    print("Invalid mobile number")

elif len(mobile) != 10:
    print("Mobile number must contain 10 digits")

elif mobile[0] not in "9876":
    print("Mobile number must start with 9, 8, 7, or 6")

else:
    print("Valid mobile number:", mobile)
