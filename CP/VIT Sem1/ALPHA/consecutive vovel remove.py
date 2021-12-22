S = input("")
vovel = ['a','e','i','o','u']
l = list(S)
x = []
for i in range(len(l)):
  if(l[i] in vovel):
    if((l[i-1] in vovel) and i!=0 ):
      x.append(i)

for i in x[::-1]:
  l.pop(i)
for i in l:
  print(i,end="")
