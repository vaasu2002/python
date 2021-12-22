''' Given an alphanumeric string S, extract maximum numeric value from that string. All the
alphabets are in lower case. Take the maximum consecutive digits as a single number''''

num,ans = 0,0
s = input("")
for i in s:
  if(i>='0' and i<='9'):
    num = num*10 + int(i)
  else:
    if(num>ans):
      ans = num
    num = 0
    
if(num>ans):
  ans = num
print(num)
