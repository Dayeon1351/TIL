import sys,heapq
input = sys.stdin.readline

n,e = map(int,input().split())
graph = [[]*(n+1)for i in range(n+1)]
for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

x,y = map(int,input().split())

def dijkstra(start):
    dist = [float('INF')] * (n+1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue,[dist[start],start])
    while queue:
        cur_dist,cur_node = heapq.heappop(queue)
        if dist[cur_node] >= cur_dist:
            for adj_node,adj_dist in graph[cur_node]:
                total_dist = cur_dist + adj_dist
                if dist[adj_node] > total_dist:
                    dist[adj_node] = total_dist
                    heapq.heappush(queue,[total_dist,adj_node])
    
    return dist

x_dist = dijkstra(x)
y_dist = dijkstra(y)

ans = min(x_dist[1] + x_dist[y] + y_dist[n],y_dist[1] + y_dist[x] + x_dist[n])
print(ans if ans < float('INF') else -1)

