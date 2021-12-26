import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]

dp = [[0]*(n+1)for i in range(n+1)]

for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j]) + arr[i][j]

for i in range(m):
    x,y,dx,dy = map(int,input().split())
    print(dp[dx][dy] - (dp[x-1][dy] + dp[dx][y-1]) + dp[x-1][y-1])
    
