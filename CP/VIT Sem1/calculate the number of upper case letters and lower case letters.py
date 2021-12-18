s = input()
d = {'u':0,'l':0}
for i in s:
  if(i.isupper()):
    d['u'] = d['u'] + 1
  if(i.islower()):
   d['l'] = d['l'] + 1
print(d['u'],end=" ")
print(d['l'])
