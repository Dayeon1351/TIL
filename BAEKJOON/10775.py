import sys
input = sys.stdin.readline

g = int(input())
p = int(input())
plane = [int(input()) for _ in range(p)]
arr = [i for i in range(g+1)]

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

cnt = 0
for i in plane:
    x = find(i)
    if x == 0:
        break
    union(x,x-1)
    cnt += 1

print(cnt)