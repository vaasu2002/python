def gcd(a,b):
  l = []
  x = min(a,b)
  while(a%2==0 and b%2==0):
    a = a//2
    b = b//2
    l.append(2)
  for i in range(3,x+1,2):
    while(a%i==0 and b%i==0):
      a = a//i
      b = b//i
      l.append(i)
    return l

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
l = gcd(num1,num2)
gcd = 1
for i in l:
  gcd = gcd*i
print(gcd)
