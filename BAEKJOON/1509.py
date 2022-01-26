import sys
input = sys.stdin.readline

s = input().strip()
arr = list(s)
n = len(s)
dp = [[0]* (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][i] = 1

for i in range(1,n):
        if arr[i-1] == arr[i]:
            dp[i][i+1] = 1

for i in range(2,n):
    for j in range(1,n+1-i):
        if arr[j-1]==arr[i+j-1] and dp[j+1][i+j-1]==1:
            dp[j][i+j] = 1

result = [float('INF')] * (n+1)
result[0] = 0
for i in range(1,n+1):
    result[i] = min(result[i],result[i-1]+1)
    for j in range(i+1,n+1):
        if dp[i][j] != 0:
            result[j] = min(result[j],result[i-1]+1)

print(result[n])