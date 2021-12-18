l = input().split(" ")
d={}
for i in l:
  if(i in d):
    d[i] = d[i] + 1
  else:
    d[i] = 1
print(d)
for i in d:
  print(i,end=" ")
