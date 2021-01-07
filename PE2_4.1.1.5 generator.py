# PE2
# 4.1.1.5 Generators and closures | yield

# generator to produce the first n powers of 2

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
        
for v in powers_of_2(8):
    print(v)
print()

# list comprehensions
t = [x for x in powers_of_2(5)]
print(t)
print()

# list() function
t = list(powers_of_2(3))
print(t)
print()

# The in operator
for i in range(20):
    if i in powers_of_2(4):
        print(i)
