N = int(input(""))
A = [int(i) for i in input().split(" ")]
K = int(input(""))
key = A[K]

A.sort()
for i in range(N):
  if(key == A[i]):
    print(i)
    break
