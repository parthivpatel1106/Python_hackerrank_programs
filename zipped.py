n,x=map(int,input().split())
a=[]
for i in range(x):
    b=map(float,input().split())
    a.append(b)
y=[]
z=[]
p=[]
#avg=[]
for i in range(x):    
    y.append(list(map(float,a[i])))
    z+=[y[i]]
    p=list(map(tuple,zip(*z)))
for i in range(n):
    avg=sum(p[i])/x
    print(avg)
