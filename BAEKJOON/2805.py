import sys
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split())
tree = defaultdict(int)
for i in input().split():
    tree[int(i)] += 1

left,right = 0,max(tree.keys())

while left <= right:
    total = 0
    mid = (left + right) // 2
    for t in tree.keys():
        if t > mid:
            total += (t - mid) * tree[t]

    if total < m:
        right = mid - 1
    else:
        left = mid + 1
    
print(right)