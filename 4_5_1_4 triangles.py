# 4.5.1.4 Creating functions | testing triangles

def is_a_triangle(a, b, c):
      return a + b > c and b + c > a and c + a > b

a = float(input("Enter the first side\'s length: "))
b = float(input("Enter the second side\'s length: "))
c = float(input("Enter the third side\'s length: "))

def is_a_right_triangle(a, b, c):
      if not is_a_triangle(a, b, c):
            return False
      if c > a and c > b: #right-angle triangle.c**2 = a**2 + b**2
            return c ** 2 == a ** 2 + b ** 2
      if a > b and a > c:
            return a ** 2 == c ** 2 + b ** 2
      

print(is_a_right_triangle)

