import sys,heapq
input = sys.stdin.readline

n,m,x = map(int,input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

result = [0]*(n+1)
for i in range(1,n+1):
    dist = [float('INF')] * (n+1)
    dist[i] = 0
    queue = []
    heapq.heappush(queue,[dist[i],i])
    while queue:
        cur_dist,cur_node = heapq.heappop(queue)
        if dist[cur_node] >= cur_dist:
            for adj_node,adj_dist in graph[cur_node]:
                total_dist = cur_dist + adj_dist
                if total_dist < dist[adj_node]:
                    dist[adj_node] = total_dist
                    heapq.heappush(queue,[total_dist,adj_node])
    
    if i == x:
        for j in range(1,n+1):
            result[j] += dist[j]
    else:
        result[i] += dist[x]

print(max(result))