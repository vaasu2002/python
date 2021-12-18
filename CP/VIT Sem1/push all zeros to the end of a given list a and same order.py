# Write a Python program to push all zeros to the end of a given list a. The order of the elements should not change.
a = [int(x) for x in input().split(" ")]
non_zero = []
zero = []
for i in a:
  if(i==0):
    zero.append(i)
  else:
    non_zero.append(i)
ans = non_zero + zero
print(ans)
  
