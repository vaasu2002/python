def binary(matrix,n,m):
  for i in range(n):
    for j in range(m):
      if(matrix[i][j]==1 or matrix[i][j]==0):
        continue
      else:
        return print("NO")
  return print("YES")

n,m = [int(i) for i in input().split(" ")]
matrix = []
for i in range(n):
  row = []
  row = [int(x) for x in input().split(" ")]
  matrix.append(row)

binary(matrix,n,m)
