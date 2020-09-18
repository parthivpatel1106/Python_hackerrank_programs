import collections
x=int(input())
y=collections.Counter(map(int,input().split()))
k=list(y.keys())
#print(k)
v=list(y.values())
#print(v)
n=int(input())
s=[]
for i in range(n):
    s.append(list(map(int,input().split())))
    #print(s)
amt=0
for j in range(len(s)):
    for i in range(len(k)):
        if(k[i]==s[j][0] and v[i]!=0):
            v[i]=v[i]-1
            amt=amt+s[j][1]
print(amt)
                

