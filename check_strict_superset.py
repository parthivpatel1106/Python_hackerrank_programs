set_a=set(map(int,input().split()))
n=int(input())
y=[]
for i in range(n):
    other_set=set(map(int,input().split()))
    x=set_a.issuperset(other_set)
    y.append(x)
print(all(y)) #all function give true decision if all output is true