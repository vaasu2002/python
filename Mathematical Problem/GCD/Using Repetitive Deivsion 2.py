def gcd(a,b):
    l=[]
    x = a
    y = b
    if(b>a):
        x = b
        y = a
    while(a%2==0 and b%2==0):
        a,b = a//2,b//2
        l.append(2)
    for i in range(3,y+1,2):
        while(a%i==0 and b%i==0):
            a,b = a//i,b//i
            l.append(i)
    
    return l
a = 12
b = 28
l = gcd(28,12)
gcd = 1
for i in l:
    gcd = gcd*i
print(gcd)
        
