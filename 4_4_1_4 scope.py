# 4.4.1.4 Scopes in Python

def my_function(my_list_1):
      print("Print #1", my_list_1)
      print("Print #2", my_list_2)
      my_list_1 = [0, 1]
      print("Print #3", my_list_1)
      print("Print #4", my_list_2)

my_list_2 = [2, 3]
my_function(my_list_2)
print("print #5", my_list_2)
      
