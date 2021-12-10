''' Question _ 1:
Zack has messed up all his shoes. He has N shoes (single shoe, not paired).  You have to search for the partner of each shoe. Find the maximum pair you can make out of them.
You will be given a description of each shoe i.e. the size of the shoes and if it is left shoes (L) or right shoes (R). Two shoes can be paired if they are having the same size and one is left L and the other is right R.
Input:
The first line contains a single integer N. The number of shoes Next N lines has a description for each shoe, with spaces, separated size, and L/R.
    5
    1	L
    2	R
    3	L
    1	R
    2	L
Output: Constraints:
    1<=N<=1000
    Shoe size will be a positive integer less than 100.
Explanation/Solution:
In this question, we are given a number of shoes with their size and type whether it is left or right. Our aim is to make a pair of shoes which have the same size and one is left and the other is right. So we make two array one have the shoe size and other having the shoe type. Each time we compare the shoe size with other shoes and also check the types of shoes it is left or right the make one pair of shoes.

A single integer, maximum pairs can be made out of the given shoes.
    2
'''

print("INPUT")
num = int(input(""))
size = []
leg = []
for i in range(num):
  x,y = input("").split(" ")1
  size.append(x)
  leg.append(y)
ans = 0
print("OUTPUT")
for i in range(num-1):
  for j in range(i+1,num):
    if(size[i]==size[j] and leg[i]!=leg[j]):
      ans = ans + 1
print(ans)
