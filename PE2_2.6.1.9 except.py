# PE2
# 2.6.1.9 Errors - the programmer's daily bread | try-except

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
    
except ZeroDivisionError:
    print("You cannot divide by zero, sorry")
except ValueError:
    print("You must input an integer value.")
except:
    print("oh dear, something went wrong...")
print("The end")
