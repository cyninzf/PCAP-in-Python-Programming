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

