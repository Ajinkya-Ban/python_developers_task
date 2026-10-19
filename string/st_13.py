'''
Project Description:
The Text Analyzer System takes a sentence or paragraph as input from the user and performs multiple string-based analyses using Python string methods.

'''
message = input("Enter the paragraph or text =").strip()

if message == "":
    print("Please enter the paragraph")
else:
    while True:
        print("---------------Text Analyzer System------------")
        print("1.Count total characters, words, and sentences")
        print("2.Count vowels, consonants, digits, and special characters")
        print("3.Convert text to uppercase and lowercase")
        print("4.Check whether a specific word exists in the text")
        print("5.Remove extra spaces from the text")
        print("6. Exit")

        choice = int(input("Enter your choice = "))
        match choice:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("Thanks for using our app. Visit Again")
                break


