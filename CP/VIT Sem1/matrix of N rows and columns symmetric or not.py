def symm(matrix,n):
  for i in range(n):
    for j in range(n):
      if(matrix[i][j] == matrix[j][i]):
        continue
      else:
        return print("NO")
  return print("YES")



n = int(input())
matrix = []
for i in range(n):
 row=[]
 row=[int(j) for j in input().split(" ")]
 matrix.append(row)

symm(matrix,n)
