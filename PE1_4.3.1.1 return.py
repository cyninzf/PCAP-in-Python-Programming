# 4.3.1.1.Returning a result from a function

# return without an expression
def happy_new_year(wishes = True):
      print("Three...")
      print("Two.....")
      print("One.....")
      if not wishes:
            return
      print("Happy new year!")

happy_new_year()
print("\n")    

def happy_new_year(wishes = True):
      print("Three...")
      print("Two.....")
      print("One.....")
      if not wishes:
            return
      print("Happy new year!")

happy_new_year(False)
print("\n")


# return with an expression
def boring_function():
      return 123
x = boring_function()
print("The boring_function has returned its result. It's:", x)
print("\n")

def boring_function():
      print("'Boredom Mode' ON.")
      return 123

print("This lesson is interesting!")
boring_function()
print("This lesson is boring....")
