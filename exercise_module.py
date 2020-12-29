# PE2
# 1.3.1.4 Modules and Packages
# !/users/bin/env python 3

"""module.py - an example of a Python module"""

_counter = 0

def suml(the_list):
    global _counter
    _counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prodl(the_list):
    global _counter
    _counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [ i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)
