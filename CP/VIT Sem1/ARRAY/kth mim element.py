A = [int(i) for i in input().split(" ")]
k = int(input(""))
A.sort()
print(A[k-1])
print(A[-k])
