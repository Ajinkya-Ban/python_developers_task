signal = input("WHAT IS THE SIGNAL NOW?: ").lower()

match signal:
    case "green":
        print("YOU CAN GO")
    case "yellow":
        print("READY TO GO")
    case "red":
        print("STOP")
    case _:
        print("INVALID SIGNAL..Don't be over smart")
