role = input("CHOOSE YOUR ROLE(Admin/User/Guest): ").lower()

match role:
    case "admin":
        print("WELCOME ADMIN! FULL ACCESS")
    case "user":
            print("WELCOME USER! NORMAL ACCESS")
    case "guest":
            print("WELCOME GUEST! LIMITED ACCESS")
    case _:
            print("INVALID ROLE")
