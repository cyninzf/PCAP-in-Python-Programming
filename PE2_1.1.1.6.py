# PE2: 1.1.1.6 Importing a module | math

# The two namespaces (yours and the module's one) can coexist.
# We've defined our own pi and sin here.

import math

def sin(x):
    if 2 * x == pi:
        return 0.999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))
      
