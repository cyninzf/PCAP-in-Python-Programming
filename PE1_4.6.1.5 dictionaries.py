# 4.6.1.5 Tuples and dictionaries

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
      if word in dictionary:
            print(word,"->", dictionary[word])
            
      else:
            print(word,"is not in dictionary")
print()

# 4.6.1.6 Tuples and dictionaries | methods
# keys()

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
      print(key, "->", dictionary[key])

for key in sorted(dictionary.keys()):
      print(key, "->", dictionary[key])
print()

# 4.6.1.7 Tuples and dictionaries | methods
# items() and values()

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
      print(english, "->", french)

for french in dictionary.values():
      print(french)
print()

