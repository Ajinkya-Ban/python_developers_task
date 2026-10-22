amount = float(input("ENTER TOTAL SHOPPING AMOUNT: "))

if amount >= 5000:
    discount = amount * 20 / 100
elif amount >= 3000:
    discount = amount * 10 / 100
elif amount >= 1000:
    discount = amount * 5 / 100
else:
    discount = 0

final_amount = amount - discount

print("DISCOUNT AMOUNT:", discount)
print("FINAL AMOUNT:", final_amount)
