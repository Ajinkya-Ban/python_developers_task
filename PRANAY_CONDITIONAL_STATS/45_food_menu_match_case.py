print("------FOOD MENU------")
print("Choose 1: PIZZA")
print("Choose 2: MOMO")
print("Choose 3: VEG THALI")
print("Choose 4: CHICKEN HANDI")

choice = int(input("CHOOSE THE NUMBER YOU WANNA EAT (1-4): "))

match choice:
    case 1:
        print("YOU SELECTED PIZZA")
    case 2:
            print("YOU SELECTED MOMO")
    case 3:
            print("YOU SELECTED VEG THALI")
    case 4:
            print("YOU SELECTED CHICKEN HANDI")
    case _:
            print("SORRY! ITS NOT ON THE MENU")
