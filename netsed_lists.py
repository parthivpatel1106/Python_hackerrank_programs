a=[]
n=int(input())
for i in range(n):
    name=input()
    marks=float(input())
    a.append([name,marks])
print(a)
a.sort(key=lambda a: a[0])
print(a)

low=min(a,key=lambda a: a[1])
print(low)
a.remove(low)
print(a)
for i in range(0,len(a)-1):
    if(a[i][1]==low[1]):
        lower=a[i]
        print(lower)
        a.remove(lower)
        
print(a)
lowest=min(a,key=lambda a:a[1])[1]
for i in range(0,len(a)):
    if(a[i][1]==lowest):
        all=a[i][0]
        print(all)        
   