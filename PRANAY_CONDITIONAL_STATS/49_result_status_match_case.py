status = int(input("ENTER RESULT STATUS (1-4): "))

match status:
    case 1:
        print("RESULT: PASS")
    case 2:
        print("RESULT: FAIL")
    case 3:
        print("RESULT: ATKT")
    case 4:
        print("RESULT: DISTINCTION")
    case _:
        print("INVALID RESULT STATUS")
