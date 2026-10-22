units = int(input("ENTER ELECTRICITY UNITS: "))

if units < 0:
    print("INVALID UNITS")
elif units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

if units >= 0:
    print("YOUR ELECTRICITY BILL IS:", bill)
