def prime(num):
    l=[]
    while(num%2 == 0):
        l.append(2)
        num = num//2
    i = 3
    while(i*i<=num):
        if(num%i==0):
            l.append(i)
            num = num//i
        else:
            i = i + 2
    if(num!=0):
        l.append(num)
    return l

base = 3
exp = 45
l = prime(exp)
print(l)
for i in l:
    p = 1
    while(i>0):
        p = p*base
        i = i - 1
    base =p
print(p)
