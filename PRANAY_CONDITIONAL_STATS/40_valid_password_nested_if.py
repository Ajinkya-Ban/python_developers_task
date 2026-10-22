password = input("ENTER YOUR PASSWORD: ")

if(password != ""):
    if(len(password)>=8):
        print("PASSWORD IS VALID")
    else:
        print("PASSWORD MUST CONTAIN AT LEAST 8 CHARACTERS")
else:
    print("PASSWORD CAN'T BE EMPTY")
