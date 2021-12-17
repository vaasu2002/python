METHOD 1

R,C=map(int,input().split())
a = 1
for i in range(R):
  for i in range(C):
    print(a,end="")
    a  = a + 1
  print()

  
  
Method 2

R,C=map(int,input().split())
l = []
k = 1
for i in range(R):
  x = []
  for j in range(C):
    x.append(k)
    k = k + 1
  l.append(x)

for i in range(R):
  for j in range(C):
    print(l[i][j],end="")
  print()
