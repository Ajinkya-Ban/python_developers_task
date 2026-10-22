choice = int(input("ENTER YOUR LANGUAGE CHOICE (1-4): "))

match choice:
    case 1:
        print("YOU SELECTED ENGLISH")
    case 2:
        print("YOU SELECTED HINDI")
    case 3:
        print("YOU SELECTED MARATHI")
    case 4:
        print("YOU SELECTED SANSKRIT")
    case _:
        print("INVALID LANGUAGE CHOICE")
