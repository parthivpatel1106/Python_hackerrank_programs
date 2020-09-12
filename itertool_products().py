import itertools
A= map(int,input().split())
B= map(int,input().split())
x=itertools.product(A,B)
for i in x:
    print(i,end=" ") # for output in same in line