a=int(input("enter value"))
b=int(input("enter value"))
c=int(input("enter value"))
if (a>b) and (a>c):
     print(a)
elif (b>a) and (b>c):
     print(b)
else:
     print(c)




def large(a,b,c):
     if (a > b) and (a > c):
          print(a)
     elif (b > a) and (b > c):
          print(b)
     else:
          print(c)
     return 0
large(2,3,4)
large(9,4,3)
large(7,31,6)