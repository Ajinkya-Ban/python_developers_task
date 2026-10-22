day = int(input("ENTER THE NUMBER (1-7): "))

match day:
    case 1:
        print("MONDAY")
    case 2:
        print("TUE")
    case 3:
        print("WED")
    case 4:
        print("THU")
    case 5:
        print("FRI")
    case 6:
        print("SAT")
    case 7:
        print("SUNDAY")
    case _:
        print("INVALID DAY NUMBER")
