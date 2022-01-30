import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[float('INF')] * (1<<n) for _ in range(n)]

def dfs(x,visited):
    if visited == (1<<n) - 1:
        if graph[x][0]:
            return graph[x][0]
        else:
            return float('INF')

    if dp[x][visited] != float('INF'):
        return dp[x][visited]
    
    for i in range(1,n):
        # 가는 경로가 있고 방문하지 않은 경우
        if graph[x][i] and not visited & (1 << i): 
            dp[x][visited] = min(dp[x][visited],dfs(i,visited | 1 << i )+ graph[x][i])

    return dp[x][visited]

print(dfs(0,1))

