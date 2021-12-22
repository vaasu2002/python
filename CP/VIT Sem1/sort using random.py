from random import randint
n = int(input(""))
A = [int(i) for i in input().split(" ")]

loop = True
while(loop):
  i = randint(0,n-1)
  j = randint(0,n-1)
  A[i],A[j] = A[j],A[i]
  w = 0
  for k in range(n):
    for r in range(k+1,n):
      if(A[k]<A[k+1]):
        loop = False
      else:
        loop = True
        break
    if(loop == True):
      break

for i in A:
  print(i,end=" ")
