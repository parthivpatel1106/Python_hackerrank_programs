import textwrap
def wrap(s,n):
    return textwrap.fill(s,n)
s=input()
n=int(input())
result=wrap(s,n)
print(result)