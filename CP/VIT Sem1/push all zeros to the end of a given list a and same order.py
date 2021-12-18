# Write a Python program to push all zeros to the end of a given list a. The order of the elements should not change.
# WITHOUT APPEND

l = [int(x) for x in input().split(" ")]
c_zero,non_zero = 0,0
for i in l:
  if(i==0):
    c_zero = c_zero + 1
  else:
    non_zero = non_zero + 1
non = [False for i in range(non_zero)]
j = 0
for i in l:
  if(j<non_zero):
    if(i!=0):
      non[j] = i
      j = j + 1
zero = [0 for i in range(c_zero)]
print(non + zero)




# APPEND
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
  
