n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
print(student_marks)
query_name = input()
n=student_marks.keys()
n_list=list(n)
print(n_list)
s=student_marks.values()
s_list=list(s)
print(s_list)
for i in range(0,len(n_list)):
    if(n_list[i]==query_name):
        avg=(s_list[i][0]+s_list[i][1]+s_list[i][2])/3
        print("{:.2f}".format(avg))
    else:
        print("not working")