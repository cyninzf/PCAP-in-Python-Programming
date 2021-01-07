# PE2
# 4.1.1.9 Generators and closures | The lambda function

# A lambda function is a function without a name.
# Such a clause returns the value of the expression when taking into account
#       the current value of the current lambda argument
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))
print()

# 4.1.1.10 Generators and closures | The lambda function

def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')
        
def poly(x):
    return 2 * x **2 - 4 * x + 2

print_function([x for x in range(-2, 3)], poly)
print()

def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')
        
print_function([x for x in range(-2, 3)], lambda x: 2 * x **2 - 4 * x + 2)
