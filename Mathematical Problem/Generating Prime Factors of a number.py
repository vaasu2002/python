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
num = int(input("Enter the number: "))
print(prime_factor(num))
