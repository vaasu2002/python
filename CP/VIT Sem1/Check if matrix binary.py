def Binary(matrix):
  for i in range(len(matrix)):
    for j in matrix[i]:
      if(j==0 or j == 1):
        continue
      else:
        return print("NO")
  return print("YES")





n,m=[int(i) for i in input().split(" ")]
matrix = []
for i in range(n):
 row=[]
 row=[int(j) for j in input().split(" ")]
 matrix.append(row)



Binary(matrix)
