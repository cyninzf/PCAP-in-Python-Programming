# PE2
# 1.2.1.3 Useful modules | math

from math import pi, radians, degrees, sin, cos, tan, asin, e, exp, log

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
print()
print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 *log(2)))
print(log(e, e) == exp(0))
