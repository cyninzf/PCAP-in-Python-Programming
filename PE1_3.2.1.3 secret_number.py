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
number = int(input("What is the secret number? "))

while number:
    if number != secret_number:
        print("Ha, ha! You're stuck in my loop!")
        number = int(input("What is the secret number? "))
    else:
        print("Well done, muggle! You are free now.")
        break
    
