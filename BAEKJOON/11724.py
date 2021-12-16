from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic = defaultdict(list)
for i in range(m):
    k,v = map(int,input().split())
    dic[k] += [v]
    dic[v] += [k]

visited = [0]*(n+1)
def bfs(cur_node):
    queue = deque([cur_node])
    while queue:
        cur_node = queue.popleft()
        if visited[cur_node] == 0:
            visited[cur_node] = 1
            for adj_node in dic[cur_node]:
                    queue.append(adj_node)

cnt = 0
for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)