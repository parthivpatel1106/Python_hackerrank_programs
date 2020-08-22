n=int(input())
alpha='abcdefghijklmnopqrstuvwxyz'
print(alpha[n-1])
for i in range(n):
    print(alpha[n-1].center((n**2),'-'))