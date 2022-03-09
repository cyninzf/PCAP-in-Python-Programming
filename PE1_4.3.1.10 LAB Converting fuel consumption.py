# 4.3.1.19 LAB: Converting fuel consumption
def liters_100km_to_miles_gallon(liters):
      mpg = (3.785411784 / liters)*(100000 / 1609.344)
      return mpg
      
def miles_gallon_to_liters_100km(miles):
      lper100km = 3.785411784 / (miles * 1609.344 / 100000)
      return lper100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
