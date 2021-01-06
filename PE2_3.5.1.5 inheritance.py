# PE2
# 3.5.1.5 OOP Fundamentals: Inheritance

# issubclass
# The function returns True if ClassOne is a subclass of ClassTwo,
# and False otherwise
class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end = "\t")
    print()

print()

# isinstance()
# Being an instance of a class means that the object has been prepared
# using a recipe contained in either the class or one of its superclasses.
class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end = "\t")
    print()
