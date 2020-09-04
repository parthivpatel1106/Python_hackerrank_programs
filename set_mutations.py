n=int(input())
a=set(map(int,input().split()))
m=int(input())
for i in range(m):
    s,j=input().split()
    x=set(map(int,input().split()))
    if(s=='intersection_update'):
        a.intersection_update(x)
    elif(s=='difference_update'):
        a.difference_update(x)
    elif(s=='symmetric_difference_update'):
        a.symmetric_difference_update(x)
    elif(s=='update'):
        a.update(x)
print(sum(a))
        
