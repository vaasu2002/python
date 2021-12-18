n = input()
one,zero = 0,0
for i in n:
  if(i==0):
    zero = zero + 1
  else:
    one = one + 1
if(one==1 or zero==1):
  print("YES")
else:
  print("NO")
