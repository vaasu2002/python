def symmetric(matrix,n):
  for i in range(n):
    for j in range(n):
      if(i!=j):
        if(matrix[i][j] != matrix[j][i]):
          return print("NO")
  print("YES")



n = int(input(""))
matrix = []
for i in range(n):
  x = [int(i) for i in input().split(" ")]
  matrix.append(x)

symmetric(matrix,n)
