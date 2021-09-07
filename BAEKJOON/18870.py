import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
sorted_arr = sorted(set(arr))
dic = {sorted_arr[i] : i for i in range(len(sorted_arr))}
for i in arr:
    print(dic[i],end=" ")
