import sys
input = sys.stdin.readline

def getLength(a,b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

result = (float('INF'),0)
for i in range(n):
    max_len = 0
    for j in range(n):
        if i != j:
            max_len = max(max_len,getLength(arr[i],arr[j]))

    if max_len < result[0]:
        result = (max_len,i)

print(*arr[result[1]])