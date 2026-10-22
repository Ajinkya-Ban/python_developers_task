# 29. Replace Word In Sentence

sentence = input("ENTER A SENTENCE: ")
old_word = input("ENTER THE WORD TO REPLACE: ")
new_word = input("ENTER THE NEW WORD: ")

words = sentence.split()
updated_words = [new_word if word == old_word else word for word in words]
print("UPDATED SENTENCE:", " ".join(updated_words))
