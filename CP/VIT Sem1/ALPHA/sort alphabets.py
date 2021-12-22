'''Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.'''

s = input("").split(",")
s.sort()
for i in s:
  print(i,end=" ")
