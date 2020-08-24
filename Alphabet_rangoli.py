n=int(input())
alpha='abcdefghijklmnopqrstuvwxyz'
for i in range(n,0,-1):
    s='-'.join(alpha[i-1:n])
    x=s[::-1]+s[1:]
    y=x.center((n*4)-3,'-')
    print(y)
for i in range(1,n):
    s='-'.join(alpha[i:n])
    x=s[::-1]+s[1:]
    y=x.center((n*4)-3,'-')
    print(y)