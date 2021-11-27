def prime_factor(num):
  l = []
  while(num%2 == 0):
    l.append(2)
    num = num //2
  i = 3
  while(i*i<=num):
    if(num%i==0):
      l.append(i)
      num = num // i
    else:
      i = i + 2
  if num!=0:
    l.append(num)
  return l
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
factor1 = prime_factor(num1)
factor2 = prime_factor(num2)
print(f"Prime factor of {num1} are {factor1} and that of {num2} are {factor2}")
common_factor=[]
for i in factor1:
  for j in factor2:
    if(i == j):
      common_factor.append(i)
      factor2.remove(j)
      break
print(f"Common factors of {num1} and {num2} are {common_factor}")

gcd = 1
for i in common_factor:
  gcd = gcd*i 
print(gcd)     
