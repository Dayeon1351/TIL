import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split()))for i in range(n)]

for i in range(1,len(arr)):
    arr[i][0] += min(arr[i-1][1],arr[i-1][2])
    arr[i][1] += min(arr[i-1][0],arr[i-1][2])
    arr[i][2] += min(arr[i-1][0],arr[i-1][1])

print(min(arr[n-1]))