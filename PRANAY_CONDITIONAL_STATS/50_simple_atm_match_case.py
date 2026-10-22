balance = 5000

print("===== ATM MENU =====")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("ENTER YOUR CHOICE: "))

match choice:
    case 1:
        print("YOUR BALANCE IS:", balance)

    case 2:
        amount = int(input("ENTER DEPOSIT AMOUNT: "))
        if amount > 0:
            balance = balance + amount
            print("AMOUNT DEPOSITED SUCCESSFULLY")
            print("YOUR NEW BALANCE IS:", balance)
        else:
            print("INVALID AMOUNT")

    case 3:
        amount = int(input("ENTER WITHDRAWAL AMOUNT: "))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("PLEASE COLLECT YOUR CASH")
            print("YOUR NEW BALANCE IS:", balance)
        else:
            print("INVALID AMOUNT OR INSUFFICIENT BALANCE")

    case 4:
        print("THANK YOU FOR USING OUR ATM")

    case _:
        print("INVALID CHOICE")
