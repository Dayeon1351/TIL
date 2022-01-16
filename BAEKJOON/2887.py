import sys,heapq
input = sys.stdin.readline

n = int(input())
x = []
y = []
z = []

for i in range(n):
    a,b,c = map(int,input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))

x.sort()
y.sort()
z.sort()

# 크루스칼
# graph = []
# root = [i for i in range(n+1)]

# for i in range(1,n):
#     graph.append((abs(x[i-1][0]-x[i][0]),x[i-1][1],x[i][1]))
#     graph.append((abs(y[i-1][0]-y[i][0]),y[i-1][1],y[i][1]))
#     graph.append((abs(z[i-1][0]-z[i][0]),z[i-1][1],z[i][1]))
    

# graph.sort()

# def find(x):
#     if root[x] == x:
#         return x
#     return find(root[x])

# def union(a,b):
#     a = find(a)
#     b = find(b)
#     if a < b:
#         root[b] = a
#     else:
#         root[a] = b

# result = 0
# for cost_node in graph:
#     cost,cur_node,next_node = cost_node
#     if find(cur_node) != find(next_node):
#         union(cur_node,next_node)
#         result += cost

# print(result)

#프림
graph = [[] for _ in range(n)]
for i in range(1,n):
    graph[x[i-1][1]].append((abs(x[i-1][0]-x[i][0]),x[i][1]))
    graph[x[i][1]].append((abs(x[i-1][0]-x[i][0]),x[i-1][1]))
    graph[y[i-1][1]].append((abs(y[i-1][0]-y[i][0]),y[i][1]))
    graph[y[i][1]].append((abs(y[i-1][0]-y[i][0]),y[i-1][1]))
    graph[z[i-1][1]].append((abs(z[i-1][0]-z[i][0]),z[i][1]))
    graph[z[i][1]].append((abs(z[i-1][0]-z[i][0]),z[i-1][1]))


cnt = 0
result = 0
heap = [[0,1]]
visited = [False] * n
while heap:
    if cnt == n:
        break
    cur_cost,cur_node = heapq.heappop(heap)
    if not visited[cur_node]:
        visited[cur_node] = True
        result += cur_cost
        cnt += 1
        for next_cost_node in graph[cur_node]:
            if not visited[next_cost_node[1]]:
                heapq.heappush(heap,next_cost_node)

print(result)
