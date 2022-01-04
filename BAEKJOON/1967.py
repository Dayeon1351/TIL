from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


def getMaxWei(start):
    queue = deque([[start,0]])
    visited = [False] * (n+1)
    visited[start] = True
    result = [0,0]
    while queue:
        cur_node,cur_wei = queue.popleft()
        for adj_node,adj_wei in graph[cur_node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                next_wei = cur_wei+adj_wei
                queue.append([adj_node,next_wei])
                if result[1] < next_wei:
                    result = adj_node,next_wei
                    
    return result

print(getMaxWei(getMaxWei(1)[0])[1])