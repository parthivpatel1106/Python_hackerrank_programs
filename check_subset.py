t=int(input())
for i in range(t):
    a=int(input())
    set_a=set(map(int,input().split()))
    b=int(input())
    set_b=set(map(int,input().split()))
    if(set_a.issubset(set_b)==True):
        print("True")
    else:
        print("False")