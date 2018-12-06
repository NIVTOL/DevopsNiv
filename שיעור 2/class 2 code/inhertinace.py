class Vehicle:
    def general_usage(self):
        print ("general use Transportation")

class Car (Vehicle):
    def __init__(self):
        print ("i am a car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):

        print("specific use : commet to work and vaction with family ")

class Moto (Vehicle):
     def __init__(self):
         print ("i am a moto")
         self.wheels = 2
         self.has_roof = False

     def specific_usage(self):

        print("specific use: commet to race and personal use")

c = Car()
c.general_usage()
c.specific_usage()

print (issubclass(Car,Moto))
print (issubclass(Car,Vehicle))

m = Moto()
m.general_usage()
m.specific_usage()


