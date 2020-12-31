# PE2
# 2.5.1.3 Four simple programs
# number processor

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0

try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, " is not a number.")

