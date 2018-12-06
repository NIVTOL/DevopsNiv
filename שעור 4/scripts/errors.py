# try:
#     f = open("C:/TEST1/readme.txt",'r')
#     f.write("12")
# except IOError:
#     print ("Error:cant find")
# opt1
# My_file = open("C:/TEST1/readme.txt",'r')
# content = My_file.read()
# print (content)
# try:
# option2
try:
    f = open("C:/TEST1/readme.txt",'r+')
    f.write("12")
except:
    print ("Error:cant find")
print("niv")