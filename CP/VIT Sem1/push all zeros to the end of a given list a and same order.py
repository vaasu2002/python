# Write a Python program to push all zeros to the end of a given list a. The order of the elements should not change.
a = [int(i) for i in input().split(" ")]
l=[]
count = 0
for i in a:
  if(i!=0):
    l.append(i)
  else:
    count = count + 1
ans = []
zero = []
for j in range(count):
  zero.append(0)
ans = l + zero
for i in ans:
  print(i,end=" ")
  
