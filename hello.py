no1 = int(input("Enter no1"))
no2= int(input ("Enter no2"))
if(no1 < no2):
    sum  = no1+no2
    print(sum)
elif(no1> 5):
    sub = no1-no2
    print(sub)
else:
    print("Hello")


for i in range(5,10,2):
    print("hello")

for i in range(1,50):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)