month = int(input("ENTER MONTH NUMBER (1-12): "))
year = int(input("ENTER YEAR: "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 DAYS")
    case 4 | 6 | 9 | 11:
        print("30 DAYS")
    case 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print("29 DAYS")
        else:
            print("28 DAYS")
    case _:
        print("INVALID MONTH NUMBER")
