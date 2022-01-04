from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
graph = [[] for i in range(v+1)]
for i in range(v):
    arr = list(map(int,input().split()))
    graph[arr[0]] = [[arr[j],arr[j+1]] for j in range(1,len(arr),2) if arr[j] != -1]

def getMaxWei(start):
    queue = deque([[start,0]])
    visited = [False] * (v+1)
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