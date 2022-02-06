import sys
input = sys.stdin.readline


def init(start,end,node):
    if start == end:
        segmentTree[node] = arr[start]
        return segmentTree[node]
        
    mid = (start + end) // 2
    segmentTree[node] = init(start,mid,node*2) + init(mid+1,end,node*2+1)
    return segmentTree[node]

def update(start,end,node,idx,val):
    if idx < start or idx > end:
        return
    segmentTree[node] += val
    if start != end:
        mid = (start + end) // 2
        update(start,mid,node*2,idx,val)
        update(mid+1,end,node*2+1,idx,val)
    

def getPrefixSum(start,end,node,left,right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return segmentTree[node]
    mid = (start + end) // 2
    return getPrefixSum(start,mid,node*2,left,right) + getPrefixSum(mid+1,end,node*2+1,left,right) 


n,m,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]
segmentTree = [0] * (n * 4)

init(0,n-1,1)

for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        b -= 1
        val = c - arr[b]
        arr[b] = c
        update(0,n-1,1,b,val)
    else:
        print(getPrefixSum(0,n-1,1,b-1,c-1))
    
