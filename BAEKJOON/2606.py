import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())

computer = defaultdict(list)
for i in range(m):
    k,v = map(int,input().split())
    computer[k] += [v]
    computer[v] += [k]

stack = [1]
visited = []
while stack:
    cur_node = stack.pop()
    visited.append(cur_node)
    for adj_node in computer[cur_node]:
        if adj_node not in stack and adj_node not in visited:
            stack.append(adj_node)

print(len(visited)-1)

