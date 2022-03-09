# 4.5.1.4 Creating functions | testing triangles

def is_a_triangle(a, b, c):
      return a + b > c and b + c > a and c + a > b

a = float(input("Enter the first side\'s length: "))
b = float(input("Enter the second side\'s length: "))
c = float(input("Enter the third side\'s length: "))

if is_a_triangle(a, b,c):
      print("Yes, it can be a triangle.")
else:
      print("No, it can\'t be a triangle.\n")

# right-angle triangle
def is_a_right_triangle(a, b, c):
      if not is_a_triangle(a, b, c):
            return False
      if c > a and c > b: #right-angle triangle.c**2 = a**2 + b**2
            return c ** 2 == a ** 2 + b ** 2
      if a > c and a > b:
            return a ** 2 == c ** 2 + b ** 2

if not is_a_triangle(a, b, c):
      print("No, it can\'t be a triangle.\n")            
elif is_a_right_triangle(a, b,c):
      print("Yes, it is a right-angle triangle.")
else:
      print("No, it isn\'t a right-angle triangle.\n")

