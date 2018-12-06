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
