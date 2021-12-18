s = input()
num1,ans=0,0
for i in s:
    if(i<='9' and i>='0'):
        num1 = num1*10 + int(i)
    else:
        if(num1>ans):
            ans = num1
        num1 = 0
if(num1>ans):
    ans = num1
print(ans)
