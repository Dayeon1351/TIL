from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
point = [0] * (n+1)
for _ in range(m):
    pd = tuple(map(int,input().split()))
    for i in range(2,pd[0]+1):
        graph[pd[i-1]].append(pd[i])
        point[pd[i]] += 1

queue = deque([i for i in range(1,n+1) if point[i] == 0])

visited = []
while queue:
    cur_node = queue.popleft()
    for i in graph[cur_node]:
        point[i] -= 1
        if point[i] == 0:
            queue.append(i)
    visited.append(cur_node)

print("\n".join(map(str,visited)) if len(visited) == n else 0)