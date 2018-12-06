# class Employee:
#     EmpCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.EmpCount += 1
#
#     def displayCount(self):
#         print (" Total employees %d" % Employee.EmpCount)
#
#
#     def displayEmployee(self):
#         print("Name: " , self.name, ", Salary: ", self.salary)
#
#
# emp1 = Employee( "niv" , 10000 )
# emp2 = Employee( "yos" , 20000 )
# emp3 = Employee( "yosi" , 20000 )
#
# emp1.displayEmployee()
# emp2.displayEmployee()
# emp3.displayEmployee()
# emp1.displayCount()
#
class retangle:

    def __init__(self ,width,highest):
        self.width = width
        self.highest = highest

    def setwidthhighest(self, w, h):
        self.width = w
        self.highest = h

    def displayme(self):
      print ("my highest: ", self.highest, ", my width :", self.width)

r1 = retangle(10, 20)
r2 = retangle(40, 60)

r1.displayme()
r2.displayme()

r1.setwidthhighest(3,10)
r1.displayme()

