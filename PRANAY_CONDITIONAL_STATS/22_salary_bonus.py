salary = float(input("ENTER YOUR SALARY: "))
years = int(input("ENTER THE YEARS OF SERVICE: "))

if years >= 5:
    bonus = salary *10/100
    print("YOUR BONUS IS: ", bonus)
else:
    print("YOU ARE NOT ELIGIBLE FOR BONUS")
