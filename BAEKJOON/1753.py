import sys,heapq
input = sys.stdin.readline

v,e = map(int,input().split())
k = int(input())
dist = [float('INF')]*(v+1)
node = [[] for i in range(v+1)]

for i in range(e):
    a,b,c = map(int,input().split())
    node[a].append([b,c])


queue = []
dist[k] = 0
heapq.heappush(queue,[dist[k],k])
while queue:
    cur_dist,cur_node = heapq.heappop(queue)
    if dist[cur_node] >= cur_dist:
        for adj_node,adj_dist in node[cur_node]:
            total_dist = cur_dist + adj_dist
            if total_dist < dist[adj_node]:
                dist[adj_node] = total_dist
                heapq.heappush(queue,[total_dist,adj_node])


for i in range(1,v+1):
    result = "INF" if dist[i] == float('INF') else dist[i]
    print(result)