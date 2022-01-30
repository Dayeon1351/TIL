import sys
input = sys.stdin.readline

def find(x):
    if x == arr[x]:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x < y:
        arr[y] = x
    else:
        arr[x] = y 


def ccw(x1,y1,x2,y2,x3,y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)


def cross(a,b):
    x1,y1,x2,y2 = a
    x3,y3,x4,y4 = b

    mx1,my1 = min(x1,x2),min(y1,y2)
    mx2,my2 = max(x1,x2),max(y1,y2)
    mx3,my3 = min(x3,x4),min(y3,y4)
    mx4,my4 = max(x3,x4),max(y3,y4)

    abc = ccw(x1,y1,x2,y2,x3,y3)
    abd = ccw(x1,y1,x2,y2,x4,y4)
    cda = ccw(x3,y3,x4,y4,x1,y1)
    cdb = ccw(x3,y3,x4,y4,x2,y2)


    if abc*abd == 0 and cda*cdb == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return True
    else:
        if abc*abd <= 0 and cda*cdb <= 0:
            return True

    return False



n = int(input())
position = [list(map(int,input().split())) for _ in range(n)]
arr = [i for i in range(n)]

for i in range(n-1):
    for j in range(i+1,n):
        if cross(position[i],position[j]):
            union(i,j)


cnt = 0
group_cnt = [0] * n
for i in range(n):
    if i == arr[i]:
        cnt += 1
    group_cnt[find(i)] += 1

print(cnt)
print(max(group_cnt))