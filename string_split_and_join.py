def split_join(a):
    a=a.split(" ")
    a="-".join(a)
    return a
a=input()
result=split_join(a)
print(result)