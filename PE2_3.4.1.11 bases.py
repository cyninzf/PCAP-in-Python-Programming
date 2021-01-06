# PE2
# 3.4.1.11 SECTION SUMMARY
#  __bases__ is a tuple containing a class's superclasses.

class Sample:
    def __init__(self):
        self.name = Sample.__name__
    def myself(self):
        print("My name is " + self.name + " living in a " + Sample.__module__)


obj = Sample()
obj.myself()
