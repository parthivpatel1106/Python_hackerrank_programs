"""
The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:
Input Format:
The first line contains an integer.
Output Format:
Print the list of integers from  through  as a string, without spaces.
"""

num = int(input())
for i in range(num):
    i+=1
    print(i,end="")