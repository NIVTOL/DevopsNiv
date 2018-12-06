# class Car:
#         def __init__(self, manafactor,):
#                 self.manafactor=manafactor
#
#
# def main():
#    x = Car("volvo")
#    print(x.manafactor)
# if __name__ == '__main__':
#  main()
 #targil2
# for number in range(1, 11):
#     print(number)
# option1
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# targil that print 1 - 10
# targil 3
# the answer is yes - in pathon we have no linit on intherinace
# Targil 4
# In Python a class can inherit from more than one class
# Targil 5
class Car:
 def __init__(self, manafactor,engine,color,tier):
           self.manafactor = manafactor
           self.engine = engine
           self.color = color
           self.tier = tier

def main():
     x = Car("volvo","1600","blue","30psi")
     print("the manafactor is",x.manafactor)
     print("the engine is ",x.engine)
     print("the color",x.color)
     print(" the tier is",x.tier)

if __name__ == '__main__':
  main()

