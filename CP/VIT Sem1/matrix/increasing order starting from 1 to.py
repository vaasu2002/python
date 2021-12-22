row,column = [int(i) for i in input().split(" ")]
l = row*column
z = 1
for i in range(row):
  for j in range(column):
    print(z,end=" ")
    z = z + 1
  print()
