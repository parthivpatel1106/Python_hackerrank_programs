m,n=map(int,input().split())
print(m,n)
cstr='.|.'
center_name="WELCOME"
for i in range(m):
    if(i%2!=0):
        print((cstr*(i)).center(n,'-'))
print(center_name.center(n,'-'))
for i in range(m,0,-1):  #backward loop
    if(i%2!=0 and i!=m): #to remove m line
        print((cstr*(i)).center(n,'-'))        