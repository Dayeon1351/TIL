import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    arr = [list(map(int,input().split()))for i in range(2)]
    for j in range(1,n):
        if j == 1:
            arr[0][j] += arr[1][j-1]
            arr[1][j] += arr[0][j-1]
        else:
            arr[0][j] += max(arr[1][j-1],arr[1][j-2])
            arr[1][j] += max(arr[0][j-1],arr[0][j-2])

    print(max(arr[0][n-1],arr[1][n-1]))