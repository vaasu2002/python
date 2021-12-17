a = [int(i) for i in input().split()]
ans = []
for i in a:
 if(i%5!=0):
  ans.append(i)
for i in range(len(ans)):
 if(i==len(ans)-1):
  print(ans[i],end="")
 else:
  print(ans[i],end=" ")
  
# print(" ".join(map(str,b)),end='')  
  
  
  
  
  
'''
2 4 5 20 25 3 467 100
2 4 3 467
'''
