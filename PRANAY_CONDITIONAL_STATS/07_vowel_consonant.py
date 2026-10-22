v = input("ENTER THE CHARACTER: ").upper()

if len(v) != 1 or not v.isalpha():
    print("PLEASE ENTER ONE ALPHABET CHARACTER")
elif v in "AEIOU":
    print(f"{v} is a VOWEL")
else:
    print(f"{v} is CONSONANT")
