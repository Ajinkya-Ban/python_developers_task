'''
Project Description:
The Text Analyzer System takes a sentence or paragraph as input from the user and performs multiple string-based analyses using Python string methods.

'''
text = input("Enter the paragraph or text =").strip()

if text == "":
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
                char_count = len(text)
                word_count = len(text.split())
                sentence_count = text.count('.') + text.count('!') + text.count('?')

                print("Total Characters:", char_count)
                print("Total Words:", word_count)
                print("Total Sentences:", sentence_count)
            case 2:
                 vowels = 0
                 consonants = 0
                 digits = 0
                 special = 0

                for i in text:
                    if i.lower() in "aeiou":
                        vowels += 1
                    elif i.isalpha():
                        consonants += 1
                    elif i.isdigit():
                        digits += 1
                    elif i != " ":
                        special += 1

                print("Vowels:", vowels)
                print("Consonants:", consonants)
                print("Digits:", digits)
                print("Special Characters:", special)
            case 3:
                  print("Uppercase:", text.upper())
                  print("Lowercase:", text.lower())
            case 4:
                 word = input("Enter word to search: ")
                 if word == "":
                     print("Please enter the word")
                 else:
                     if word.lower() in text.lower():
                        print("Word exists in text")
                     else:
                        print("Word not found")
            case 5:
                 cleaned = " ".join(text.split())
                 print("Text after removing extra spaces:")
                 print(cleaned)
            case 6:
                print("Thanks for using our app. Visit Again")
                break


