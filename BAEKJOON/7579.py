import sys
input = sys.stdin.readline

n,m = map(int,input().split())
activation = [0] + list(map(int,input().split()))
disabled = [0] + list(map(int,input().split()))

max_val = sum(disabled)
dp = [[0] * (max_val+1) for _ in range(n+1)]

result = max_val
for i in range(1,n+1):
    memory = activation[i]
    cost = disabled[i]

    for j in range(1,max_val+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(memory + dp[i-1][j-cost],dp[i-1][j])

        if dp[i][j] >= m:
            result = min(result,j)

print(result)