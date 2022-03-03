# 4.2.1.6 How functions communicate with their enviroment
# Mixing positional and key word arguments

def adding(a, b, c):
      print(a, "+", b,"+", c, "=", a+b+c)

adding (3, c= 1, b = 2)
print("\n")

# 4.2.1.7 How functions communicate with their enviroment
# Parametrized functions - more details

def introduction(first_name, last_name="Smith"):
      print("Hello, my name is", first_name, last_name)

introduction("James", "Doe")
introduction("Henry")
introduction(first_name="William")

def introduction(first_name="John", last_name="Smith"):
      print("Hello, my name is", first_name, last_name)
introduction()
