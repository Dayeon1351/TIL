import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split()))for i in range(n)]
way = defaultdict(list)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            way[i] += [j]

for i in range(n):
    queue = deque([i])
    visited = [0]*n
    while queue:
        cur_node = queue.popleft()        
        for adj_node in way[cur_node]:     
            if visited[adj_node] == 0:
                visited[adj_node] = 1
                queue.append(adj_node)

    print(" ".join(map(str,visited)))
