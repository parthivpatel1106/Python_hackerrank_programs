m=int(input())
lis1=list(map(int,input().split()))
n=int(input())
lis2=list(map(int,input().split()))
x=set(lis1).difference(set(lis2))
y=set(lis2).difference(set(lis1))
z=x.union(y)
print(*sorted(z),sep="\n")