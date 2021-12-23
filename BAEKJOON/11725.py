import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
node = defaultdict(list)
for i in range(n-1):
    k,v = map(int,input().split())
    node[k] += [v]
    node[v] += [k]

parent_node = [0]*(n+1)
stack = [1]
while stack:
    cur_node = stack.pop()
    for adj_node in node[cur_node]:
        if parent_node[adj_node] == 0: 
            stack.append(adj_node) 
            parent_node[adj_node] = cur_node
    

for i in range(2,len(parent_node)):
    print(parent_node[i])

