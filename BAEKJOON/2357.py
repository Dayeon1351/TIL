import sys
input = sys.stdin.readline

def init_min_tree(start,end,node):
    if start == end:
        min_tree[node] = arr[start]
        return min_tree[node]
        
    mid = (start + end) // 2
    min_tree[node] = min(init_min_tree(start,mid,node*2),init_min_tree(mid+1,end,node*2+1))
    return min_tree[node]

def init_max_tree(start,end,node):
    if start == end:
        max_tree[node] = arr[start]
        return max_tree[node]
        
    mid = (start + end) // 2
    max_tree[node] = max(init_max_tree(start,mid,node*2),init_max_tree(mid+1,end,node*2+1))
    return max_tree[node]


def getMinVal(start,end,node,left,right):
    if left > end or right < start:
        return 1000000001

    if left <= start and right >= end:
        return min_tree[node]
    
    mid = (start + end) // 2
    return min(getMinVal(start,mid,node*2,left,right),getMinVal(mid+1,end,node*2+1,left,right))


def getMaxVal(start,end,node,left,right):
    if left > end or right < start:
        return 0
    
    if left <= start and right >= end:
        return max_tree[node]
    
    mid = (start + end) // 2
    return max(getMaxVal(start,mid,node*2,left,right),getMaxVal(mid+1,end,node*2+1,left,right))


n,m = map(int,input().split())
arr = [int(input()) for _ in range(n)]

min_tree = [0] * (n * 4)
max_tree = [0] * (n * 4)

init_min_tree(0,n-1,1)
init_max_tree(0,n-1,1)

for _ in range(m):
    a,b = map(int,input().split())
    print(getMinVal(0,n-1,1,a-1,b-1),getMaxVal(0,n-1,1,a-1,b-1))
