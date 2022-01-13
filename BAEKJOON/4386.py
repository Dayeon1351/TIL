from itertools import combinations
import sys,heapq
input = sys.stdin.readline

n = int(input())
star = [list(map(float,input().split())) for _ in range(n)]
graph = [[] for _ in range(n+1)]

for a,b in list(combinations(list(range(len(star))),2)):
    c = ((star[b][0] - star[a][0])**2 + (star[b][1] - star[a][1])**2)**0.5
    graph[a].append([c,b])
    graph[b].append([c,a])


cnt = 0
result = 0
heap = [[0,1]]
visited = [False] * (n+1)
while heap:
    if cnt == n:
        break
    cur_wei,cur_node = heapq.heappop(heap)
    if not visited[cur_node]:
        visited[cur_node] = True
        result += cur_wei
        cnt += 1
        for next_wei_node in graph[cur_node]:
            if not visited[next_wei_node[1]]:
                heapq.heappush(heap,next_wei_node)

print(round(result,2))
