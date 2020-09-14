import itertools
s,k = input().split(maxsplit=1)
x=itertools.permutations(sorted(s),int(k))
y=list(x)
str1=""
for i in range(len(y)):
    for j in range(len(y[i])): # for accept nested list 
        str1+=y[i][j] #joining string
split=[] #blank list 
for ind in range(0,len(str1),int(k)):
    split.append(str1[ind:ind+int(k)]) #split str in length of k
for ele in range(len(split)):    
    print(split[ele]) #print split answer in new lines
    
