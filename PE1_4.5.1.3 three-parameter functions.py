# 4.5.1.3 Creating functions | three-parameter functions

def is_a_triangle(a,b,c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(is_a_triangle(1,1,1))
print(is_a_triangle(1,1,3))
print("\n")

# or
def is_a_triangle(a,b,c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(is_a_triangle(1,2,1))
print(is_a_triangle(1,4,3))
print("\n")

# and
def is_a_triangle(a,b,c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(1,2,2))
print(is_a_triangle(1,2,3))
