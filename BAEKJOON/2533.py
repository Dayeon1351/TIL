import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

#dp[i][0] i가 얼리어답터일때 서브트리에서 최소값
#dp[i][1] i가 얼리어답터가 아닐때 서브트리에서 최소값
dp = [[0,0] for _ in range(n+1)]
visited = [False] * (n+1)

# # 부모 a 자식 b,c
# # a가 얼리어답터일때 b,c는 얼리어답터 여도 되고 아니여도 된다.
# # b,c 중 하나라도 얼리어답터가 아닐때 a는 얼리어답터여야 한다.
def dfs(x):
    visited[x] = True
    dp[x][0] = 1
    for node in graph[x]:
        if not visited[node]:
            dfs(node)
            dp[x][0] += min(dp[node][0],dp[node][1])
            dp[x][1] += dp[node][0]

dfs(1)
print(min(dp[1][0],dp[1][1]))