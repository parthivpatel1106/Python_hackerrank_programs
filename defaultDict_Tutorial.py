from collections import defaultdict
nm=list(map(int,input().split()))
n,m = nm[0],nm[1]
l=defaultdict(list)
a=[]
for i in range(1,n+1):
    l[input()].append(i)
for j in range(m):
    a.append(input())
#print(l)
#print(a)
for k in a: 
    if k in l.keys():
        print(*l[k])
    else:
        print("-1")