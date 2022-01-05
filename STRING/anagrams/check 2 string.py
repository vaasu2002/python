l = input().split(" ")
d1 = {}
d2 = {}
list1 = list(l[0])
for i in list1:
  if(i in d1):
      d1[i] = d1[i] + 1
  
  else:
    d1[i] = 1

list2 = list(l[1])
for i in list2:
  if(i in d2):
      d2[i] = d2[i] + 1
  else:
    d2[i] = 1

if(d1 == d2):
  print("YES")
