# 37. Find Longest Word

sentence = input("ENTER A SENTENCE: ")
words = sentence.split()

if not words:
    print("NO WORDS FOUND")
else:
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    print("LONGEST WORD:", longest)
