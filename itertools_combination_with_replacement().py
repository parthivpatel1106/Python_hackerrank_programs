import itertools
s,k=input().split(maxsplit=1)
x=itertools.combinations_with_replacement(sorted(s),int(k))
y=list(x)
str1=""
for i in range(len(y)):
    for j in range(len(y[i])):
        str1=str1+y[i][j]
print(str1)
split=[]
for _ in range(0,len(str1),int(k)):
    split.append(str1[_:_+int(k)])
for ind in range(len(split)):
    print(split[ind])