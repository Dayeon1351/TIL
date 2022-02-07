import sys
input = sys.stdin.readline


def init(start,end,node):
    if start == end:
        segmentTree[node] = arr[start]
        return segmentTree[node]
        
    mid = (start + end) // 2
    segmentTree[node] = init(start,mid,node*2) * init(mid+1,end,node*2+1) % 1000000007
    return segmentTree[node] 

def update(start,end,node,idx,val):
    if idx < start or idx > end:
        return

    if start == end:
        segmentTree[node] = val
    else:
        mid = (start + end) // 2
        update(start,mid,node*2,idx,val)
        update(mid+1,end,node*2+1,idx,val)
        segmentTree[node] = segmentTree[node*2] * segmentTree[node*2+1] % 1000000007
    

def getPrefixMulti(start,end,node,left,right):
    if left > end or right < start:
        return 1

    if left <= start and right >= end:
        return segmentTree[node]
    
    mid = (start + end) // 2
    result = getPrefixMulti(start,mid,node*2,left,right) * getPrefixMulti(mid+1,end,node*2+1,left,right) 
    return result % 1000000007

n,m,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]
segmentTree = [0] * (n * 4)

init(0,n-1,1)

for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        update(0,n-1,1,b-1,c)
    else:
        print(getPrefixMulti(0,n-1,1,b-1,c-1))
    
