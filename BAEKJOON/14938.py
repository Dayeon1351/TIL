import sys,heapq
input = sys.stdin.readline

n,m,r = map(int,input().split())
items = list(map(int,input().split()))
graph = [[] for i in range(n+1)]

for i in range(r):
    a,b,l = map(int,input().split())
    graph[a].append([b,l])
    graph[b].append([a,l])


max_val = 0
for i in range(1,n+1):
    queue = []
    dist = [float('INF')] * (n+1)
    dist[i] = 0
    heapq.heappush(queue,[dist[i],i])
    while queue:
        cur_dist,cur_node = heapq.heappop(queue)
        if dist[cur_node] >= cur_dist:
            for adj_node,adj_dist in graph[cur_node]:
                total_dist = cur_dist + adj_dist
                if total_dist < dist[adj_node]:
                    dist[adj_node] = total_dist
                    heapq.heappush(queue,[total_dist,adj_node])
    
    max_val = max(max_val,sum([items[i-1] for i in range(1,n+1) if dist[i] <= m]))

print(max_val)