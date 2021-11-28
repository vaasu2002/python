num = int(input("Enter the limit: "))
x,y,a = 0,1,0
while(a <= num):
     print(a, end = " ")
     x = y
     y = a
     a = x + y
