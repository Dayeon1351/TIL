import sys
from collections import defaultdict,deque
input = sys.stdin.readline

n,m,v = map(int,input().split())
dic = defaultdict(list)
for i in range(m):
    key,val = map(int,input().split())
    dic[key] += [val]
    dic[val] += [key]


stack = [v]
visited = []
while stack:
    cur_node = stack.pop()
    visited.append(cur_node)
    for adj_node in sorted(dic[cur_node],reverse=True):
        if adj_node not in visited:
            if adj_node in stack:
                stack.remove(adj_node)
            stack.append(adj_node)
print(" ".join(map(str,visited)))

queue = deque([v])
visited = []
while queue:
    cur_node = queue.popleft()
    visited.append(cur_node)
    for adj_node in sorted(dic[cur_node]):
        if adj_node not in visited and adj_node not in queue:
            queue.append(adj_node)
    
print(" ".join(map(str,visited)))
