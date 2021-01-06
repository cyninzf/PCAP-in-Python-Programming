# PE2
# 3.5.1.13 OOP Fundamentals: Inheritance

# Multiple inheritance

class SuperA:
    var_a = 10
    def fun_a(self):
        return 11

class SuperB:
    var_b = 20
    def fun_b(self):
        return 21

class Sub(SuperA, SuperB):
    pass

obj = Sub()

print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())

print()

# The entity defined later (in the inheritance sense) overrides the same entity
# defined earlier.

class Level1:
    var = 100
    def fun(self):
        return 101

class Level2(Level1):
    var = 200
    def fun(self):
        return 201

class Level3(Level2):
    pass

obj = Level3()

print(obj.var, obj.fun())

print()

# Python looks for object components in the following order:
#    inside the object itself;
#    in its superclasses, from bottom to top;
#    if there is more than one class on a particular inheritance path,
#       Python scans them from left to right.

class Left:
    var = 'L'
    var_left = 'LL'
    def fun(self):
        return "Left"

class Right:
    var = 'R'
    var_right = 'RR'
    def fun(self):
        return "Right"

class Sub(Left, Right):
    pass

obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())
