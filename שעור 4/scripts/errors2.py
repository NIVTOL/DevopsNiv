try:
    f = open("C:/TEST1/readme.txt",'r')
    f.write("12")
except IOError:
    print ("Error:cant find")
finally:
    print("this is game")

