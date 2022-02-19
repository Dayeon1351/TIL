from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
back_graph = [[] for _ in range(n+1)]
point = [0] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    back_graph[b].append([a,c])
    point[b] += 1
    
start,end = map(int,input().split())

queue = deque([start])
dp = [0] * (n+1)

while queue:
    cur_node = queue.popleft()
    for next_node,time in graph[cur_node]:
        point[next_node] -= 1
        dp[next_node] = max(dp[next_node],dp[cur_node]+time) 
        if point[next_node] == 0:
            queue.append(next_node)

    if cur_node == end:
        break

cnt = 0
visited = [False] * (n+1)
queue = deque([end])
while queue:
    cur_node = queue.popleft()
    for next_node,time in back_graph[cur_node]:
        if dp[cur_node] - dp[next_node] == time:
            cnt += 1

            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True


print(dp[end])
print(cnt)