string=input()
substring=input()
count=0
print(string[2:5]) #to check the substrings
print(string[4:7]) #to check the substrings
for i in range(len(string)-1):
    if(substring==string[i:len(substring)+i]):
        count=count+1
print(count)