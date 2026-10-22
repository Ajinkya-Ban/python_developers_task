grade = input("CHOOSE YOUR GRADE(A/B/C/D/F): ").upper()

match grade:
    case "A":
        print("OUTSTANDING")
    case "B":
            print("VERY GOOD")
    case "C":
            print("GOOD")
    case "D":
            print("NEED TO IMPROVE")
    case "F":
            print("FAIL! LEAVE THE EDUCATION")
    case _:
            print("INVALID GRADE")
