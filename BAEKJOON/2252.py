from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
point = [0] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    point[b] += 1
    
queue = deque([i for i in range(1,n+1) if point[i] == 0])

while queue:
    cur_node = queue.popleft()
    for i in graph[cur_node]:
        point[i] -= 1
        if point[i] == 0:
            queue.append(i)
    print(cur_node,end = " ")