def mutation(string,position,charecter):
    l=list(string)
    l[position]=charecter
    string=''.join(l)
    return string
name=input()
pos,charecter=input().split()
result=mutation(name,int(pos),charecter)
print(result)