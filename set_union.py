n=int(input())
n_no=list(map(int,input().split()))
m=int(input())
m_no=list(map(int,input().split()))
x=set(n_no) | (set(m_no)) #else you can use union keyword instead of |
print(len(x))