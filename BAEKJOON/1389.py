from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
mate = defaultdict(list)
for i in range(m):
    k,v = map(int,input().split())
    mate[k] += [v]
    mate[v] += [k]


cnt = []
for i in range(1,n+1):
    queue = deque([i])
    visited = []
    arr = [0]*(n+1)
    while queue:
        cur_node = queue.popleft()
        visited.append(cur_node)
        for adj_node in mate[cur_node]:
            if adj_node not in visited and adj_node not in queue:
                queue.append(adj_node)
                arr[adj_node] = arr[cur_node] + 1
    
    cnt.append([i,sum(arr)])

cnt.sort(key = lambda x:(x[1],[0]))
print(cnt[0][0])
            

