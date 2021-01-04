# PE2
# 2.7.1.6 The anatomy of exceptions | raise

# raise exc
def bad_fun(n):
    raise ZeroDivisionError

try:
    bad_fun(0)
except ArithmeticError:
    print('Arithmetic problem!')

print("The End")
print()

# raise
def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise

try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")
    
print("THE END")
print()

# 2.7.1.7 The anatomy of exceptions | assert
import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)
