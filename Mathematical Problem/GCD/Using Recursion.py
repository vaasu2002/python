num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
def gcd(a,b):
  if (b == 0):
    return a
  else:
    return gcd(b,a%b)
print(gcd(num1,num2))
