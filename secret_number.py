# A junior magician has picked a secret number. He has hidden it in a variable
# named secret_number. He wants everyone who run his program to play
# the Guess the secret number game.

secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
a = int(input("Enter a number: "))
while a != secret_number:
    print ("Ha ha! You're stuck in my loop!")
    a = int(input("Enter a number: "))
print("Well done, muggle! You are free now.")
    
