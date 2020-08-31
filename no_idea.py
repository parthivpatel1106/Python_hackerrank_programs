n,m=map(int,input().split())
arr=list(map(int,input().split()))
#print(arr)
a=list(map(int,input().split()))
b=list(map(int,input().split()))
#print(set(a))
#print(set(b))
x=set(a)
y=set(b)
count=0
for i in arr:
    if i in x:
        count+=1
    elif i in y:
        count-=1
print(count)