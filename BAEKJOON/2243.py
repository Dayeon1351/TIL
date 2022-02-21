from math import ceil, log2
import sys
input = sys.stdin.readline

max_val = 10 ** 6
def init(start,end,node,val):
    if start == end:
        return start
    
    mid = (start + end) // 2

    if segment[node * 2] >= val:
        return init(start,mid,node*2,val)

    else:
        return init(mid+1,end,node*2+1,val-segment[node*2])


def update(start,end,node,idx,val):
    if idx < start or idx > end:
        return

    segment[node] += val
    
    if start != end:
        mid = (start + end) // 2
        update(start,mid,node*2,idx,val)
        update(mid+1,end,node*2+1,idx,val)



n = int(input())
height = ceil(log2(max_val))
size = 2 ** (height + 1)
segment = [0] * (size)

for _ in range(n):
    temp = list(map(int,input().split()))
    if temp[0] == 1:
        index = init(0,max_val-1,1,temp[1])
        print(index)
        update(0,max_val-1,1,index,-1)
    else:
        update(0,max_val-1,1,temp[1],temp[2])
