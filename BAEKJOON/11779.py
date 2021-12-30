import sys,heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

depart,arrive = map(int,input().split())

cost = [float('INF')] * (n+1)
cost[depart] = 0
visited = [[] for i in range(n+1)]
queue = []
heapq.heappush(queue,[cost[depart],depart,[depart]])

while queue:
    cur_cost,cur_node,path = heapq.heappop(queue)
    if cost[cur_node] >= cur_cost:
        for adj_node,adj_cost in graph[cur_node]:
            total_cost = cur_cost + adj_cost
            
            if total_cost < cost[adj_node]:
                cost[adj_node] = total_cost
                visited[adj_node] = path + [adj_node]
                heapq.heappush(queue,[total_cost,adj_node,path+[adj_node]])


print(cost[arrive])
print(len(visited[arrive]))
print(" ".join(map(str,visited[arrive])))
