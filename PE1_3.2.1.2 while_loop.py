# A program that reads a sequence of numbers and counts how many numbers
# are even and how many numbers are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
counter = 5
while number:
    # Check if the number is odd.
    if number % 2:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))
    counter -=1

print ("Odd numbers count:", odd_numbers)
print ("Even numbers count:", even_numbers)
