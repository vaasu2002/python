row,column = input("").split(" ")
row = int(row)
column = int(column)
matrix = []
for i in range(row):
  x = []
  x=[int(j) for j in input().split(" ")]
  matrix.append(x)

  
for i in range(row):
  for j in range(column):
    if(i>j):
      matrix[i][j]=0

print()

for i in range(row):
  for j in range(column):
    print(matrix[i][j],end=" ")
  print()
  
  
1 2 3 
0 5 6 
0 0 9
