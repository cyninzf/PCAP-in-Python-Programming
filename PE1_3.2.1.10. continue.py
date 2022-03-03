# 3.2.1.10: the Ugly Vowel Eater

user_word = input("enter a word: ")# Prompt the user to enter a word
user_word = user_word.upper()# and assign it to the user_word variable.

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter, sep="\n")


# 3.2.1.11: the Pretty Vowel Eater
print("\n")
      
user_word = input("enter a word: ")# Prompt the user to enter a word
user_word = user_word.upper()# and assign it to the user_word variable.
word_without_vowels = ""

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter
print(word_without_vowels)
