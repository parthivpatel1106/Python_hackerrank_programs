import itertools
s=input()
for key,group in itertools.groupby(s):
    c=len(list(group)),int(key)
    print(c,end=" ")

