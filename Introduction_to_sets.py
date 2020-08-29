def average(arr):
    avg=sum(set(arr))/len(set(arr))
    return avg
n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)