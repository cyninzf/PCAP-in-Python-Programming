# 4.5.1.6 Creating functions | Factorials

def factorial_function(n):
      if n < 0:
            return None
      if n < 2:
            return 1

      product = 1
      for i in range(2, n+1):
            product *= i
      return product

for n in range (1, 6): # testing
      print(n, factorial_function(n))


# 4.5.1.7 Creating functions | Fibonacci numbers

def fib(n):
      if n < 1:
            return None
      if n < 3:
            return 1

      elem_1 = elem_2 =1
      the_sum = 0
      for i in range (3, n+1):
            the_sum = elem_1 + elem_2
            elem_1, elem_2 = elem_2, the_sum
      return the_sum
      
for n in range(1, 10): # testing
      print(n, "->", fib(n))
      

# 4.5.1.8 Creating functions | recursion
# In this field, recursion is a technique where a function invokes itself.
# The Fibonacci numbers definition is a clear example of recursion:
# Fibi = Fibi-1 + Fibi-2


def fib(n):
      if n < 1:
            return None
      if n < 3:
            return 1
      return fib(n-1) + fib(n-2)
      
for n in range(1, 10):
      print(n, "->", fib(n))

