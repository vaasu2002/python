num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
def gcd(a,b):
  x = a
  y = b
  if(b>a):
    x = b
    y = a
  if(a==b):
    return a
  while(y>0):
    r = x % y
    x = y
    y = r
  return x
print(gcd(num1,num2))
# r - remainder, dividend - a, divisor - b
