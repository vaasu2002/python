num = input()
l =[]
for i in num:
  l.append(i)
one = 0
zero = 0
for j in num:
  if(int(j)==0):
    zero = zero + 1
  if(int(j)==1):
    one = one + 1
if(zero==1 or one==1):
  print('YES')
else:
  print("NO")
