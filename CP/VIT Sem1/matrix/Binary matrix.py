def Binary(matrix,row,column):
  for i in range(row):
    for j in range(column):
      if(matrix[i][j] == 0 or matrix[i][j] == 1):
        continue
      else:
        return print("NO")
  return print("YES")
  

row,column = [int(i) for i in input().split(" ")]
matrix = []
for i in range(row):
  x = [int(j) for j in input().split(" ")]
  matrix.append(x)

Binary(matrix,row,column)
