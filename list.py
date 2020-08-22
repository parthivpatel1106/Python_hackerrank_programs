"""def flat_list(temp_list):
    for ele in temp_list:
        if(type(ele)==list):
            flat_list(temp_list)
        else:
            args.append(ele)  """
N=int(input())
l=[]
for i in range(N):
    s=input().strip().split()
    for i in range(1,len(s)):
        s[i]=int(s[i])
    if(s[0]=="append"):
        l.append(s[1])
    elif(s[0]=="print"):
        print(l)
    elif(s[0]=="insert"):
        l.insert(int(s[1]),int(s[2]))
    elif(s[0]=="remove"): 
        l.remove(s[1]) 
    elif(s[0]=="sort"):
        l.sort()  
    elif(s[0]=="pop"):
        l.pop(-1)
    elif(s[0]=="reverse"):
        l.reverse()
    
