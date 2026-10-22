# 38. Find Shortest Word

sentence = input("ENTER A SENTENCE: ")
words = sentence.split()

if not words:
    print("NO WORDS FOUND")
else:
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    print("SHORTEST WORD:", shortest)
