#isalpha()
name = input("Enter the fullname = ")
if name == "":
    print("Please enter the name")
elif not name.replace(" ","").isalpha():
    print("digits not allowed")
else:
    print(name)
