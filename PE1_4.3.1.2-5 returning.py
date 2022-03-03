# 4.3.1.2 Returning a result from a function
# A few words about None

value = None
if value is None:
      print("Sorry, you don't carry any value.")
print("\n")    

# 4.3.1.3 A few words about None: continued

def strange_function (n):
      if (n % 2 == 0):
            return True
print(strange_function(2))
print(strange_function(3))
print("\n")    

# 4.3.1.4 Returning a result from a function
# Effects and results: lists and functions

def list_sum(lst):
      s = 0
      for elem in lst:
            s += elem
      return s
print(list_sum([5,4,3]))
print("\n")    

# 4.3.1.5 Returning a result from a function
# Effects and results: lists and functions - continued

def strange_list_fun(n):
      strange_list = []
      
      for i in range(0, n):
            strange_list.insert(0,i)
      return strange_list
print(strange_list_fun(5))
