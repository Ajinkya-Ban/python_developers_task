username = input("ENTER THE USERNAME: ").lower()
password = input("ENTER THE PASSWORD: ").lower()

if (username == "admin" and password == "1234" ):
    print("LOGIN SUCCESSFUL")
else:
    print("INVALID USERNAME OR PASSWORD")
