import sys,heapq
input = sys.stdin.readline

v,e = map(int,input().split())
# 프림
# graph = [[] for _ in range(v+1)]

# for _ in range(e):
#     a,b,c = map(int,input().split())
#     graph[a].append([c,b])
#     graph[b].append([c,a])

# cnt = 0
# result = 0
# heap = [[0,1]]
# visited = [False] * (v+1)
# while heap:
#     if cnt == v:
#         break
#     cur_wei,cur_node = heapq.heappop(heap)
#     if not visited[cur_node]:
#         visited[cur_node] = True
#         result += cur_wei
#         cnt += 1
#         for next_wei_node in graph[cur_node]:
#             heapq.heappush(heap,next_wei_node)

# print(result)


# 크루스칼
graph = []
root = [i for i in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph.append([c,a,b])

graph.sort()

def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]


def union(a,b):
    rootA = find(a)
    rootB = find(b)
    if rootA < rootB:
        root[rootB] = rootA
    else:
        root[rootA] = rootB


result = 0
for cost_node in graph:
    cost,cur_node,next_node = cost_node
    if find(cur_node) != find(next_node):
        union(cur_node,next_node)
        result += cost
print(result)