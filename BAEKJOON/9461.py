import sys
input = sys.stdin.readline

dp = {1:1,2:1,3:1}
t = int(input())
for i in range(t):
    n = int(input())
    if n in dp.keys():
        print(dp[n])
    else:
        m = max(dp.keys()) + 1
        for j in range(m,n+1):
            dp[j] = dp[j-3] + dp[j-2]
        print(dp[n])