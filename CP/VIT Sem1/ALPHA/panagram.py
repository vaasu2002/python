s = input("")
check="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
check = list(check)
for i in s:
  if(i.upper() in check):
    index = check.index(i.upper())
    check[index] = False
n = 0
for i in check:
  if(i == False):
    n = n + 1
if(n==26):
  print("YES")
else:
  print("NO")
