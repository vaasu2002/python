'''Given a square matrix of N rows and columns, find out whether it is symmetric or not.
Input Format:
The first line of the input contains an integer number n which represents the number of rows
and the number of columns.
From the second line, take n lines input with each line containing n integer elements with each
element separated by a space.'''



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
