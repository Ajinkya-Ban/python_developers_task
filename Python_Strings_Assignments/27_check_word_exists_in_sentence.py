# 27. Check Word Exists In Sentence

sentence = input("ENTER A SENTENCE: ")
word = input("ENTER THE WORD TO FIND: ")

if word in sentence.split():
    print("WORD EXISTS")
else:
    print("WORD DOES NOT EXIST")
