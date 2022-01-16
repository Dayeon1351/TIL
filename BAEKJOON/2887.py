import sys,heapq
input = sys.stdin.readline

n = int(input())
planet = []
graph = [[] for _ in range(n)]
for i in range(n):
    x,y,z = map(int,input().split())
    planet.append([x,y,z,i])


for i in range(3):
    planet.sort(key=lambda x : x[i])
    a = planet[0][3]
    for j in range(1,n):
        c = abs(planet[j-1][i]-planet[j][i])
        b = planet[j][3]
        graph[a].append([c,b])
        graph[b].append([c,a])
        a = b

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