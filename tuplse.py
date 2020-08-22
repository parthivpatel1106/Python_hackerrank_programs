n = int(input())
integer_list =[int(i) for i in input().split()]
int_tuple=tuple(integer_list)
print(hash(int_tuple))