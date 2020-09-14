import itertools
s,n=input().split(maxsplit=1)
for i in range(1,int(n)+1):
    for j in itertools.combinations(sorted(s),i): #get combination by increasing i 
        x="".join(j)
        print(x)