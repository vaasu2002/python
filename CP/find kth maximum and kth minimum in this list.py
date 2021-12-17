# Given a list of numbers (integers), find second maximum and second minimum in this list.
a=[int(i) for i in input().split()]
a.sort()
k = int(input("kth max/min. k = "))
print(f"Kth max = {a[-k]}")
print(f"Kth min = {a[k-1]}")



'''
5 2 3 7 5 9 4
Sorted array [2, 3, 4, 5, 5, 7, 9]
kth max/min. k = 2
Kth max = 7
Kth min = 3
'''
