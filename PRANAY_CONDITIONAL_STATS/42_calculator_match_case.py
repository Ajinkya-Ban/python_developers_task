a = float(input("ENTER FIRST NUMBER: "))
b = float(input("ENTER SECOND NUMBER: "))
op = input("ENTER THE OPERATION (+), (-), (*), (/): ")

match op:
    case "+":
        print("RESULT: ", a+b)
    case "-":
        print("RESULT: ", a-b)
    case "*":
            print("RESULT: ", a*b)
    case "/":
            if(b != 0):
                print("RESULT: ", a/b)
            else:
                print("YOU CAN'T DIVIDE BY ZERO")
    case _:
            print("INVALID OPERATOR")
