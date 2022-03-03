# 4.3.1.9 LAB 
# Prime numbers - how to find them

def is_prime(num):
      if num <= 1:
            return False
      elif num == 2:
            return True
      elif num % 2 == 0:
            return False
      elif num == 3:
            return True
      elif num % 3 == 0:
            return False
      elif num == 5:
            return True
      elif num % 5 == 0:
            return False
      elif num % (num ** 0.5) == 0:
            return False
      else:
            return True
      
for i in range(1,300):
      if is_prime(i+1):
            print(i+1, end=" ")

