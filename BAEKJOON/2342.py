import sys
input = sys.stdin.readline

def getCost(cur,nxt):
    if cur == 0:
        return 2 if nxt != 0 else 0
    elif cur == nxt:
        return 1
    elif abs(cur-nxt) == 1 or abs(cur-nxt) == 3:
        return 3
    else:
        return 4

max_val = 400001
arr = list(map(int,input().split()))[:-1]
n = len(arr)
dp = [[[max_val for _ in range(5)]for _ in range(5)]for _ in range(n+1)]
dp[-1][0][0] = 0

for i in range(n):
    for r in range(5):
        for k in range(5):
            cost = getCost(k,arr[i])
            dp[i][arr[i]][r] = min(dp[i][arr[i]][r],dp[i-1][k][r] + cost)
    
    for l in range(5):
        for k in range(5):
            cost = getCost(k,arr[i])
            dp[i][l][arr[i]] = min(dp[i][l][arr[i]],dp[i-1][l][k] + cost)

result = max_val
for l in range(5):
    for r in range(5):
        result = min(result,dp[n-1][l][r])

print(result)
