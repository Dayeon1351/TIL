import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]
arr = [[(i,j) for j in range(m)] for i in range(n)]
visited = [[False] * m for _ in range(n)]

def find(x,y):
    if (x,y) == arr[x][y]:
        return (x,y)
    arr[x][y] = find(arr[x][y][0],arr[x][y][1])
    return arr[x][y]
    

def union(a,b,c,d):
    x = find(a,b)
    y = find(c,d)
    if x[0] < y[0]:
        arr[c][d] = (a,b)
    elif x[0] > y[0]:
        arr[a][b] = (c,d)
    else:
        if x[1] < y[1]:
            arr[c][d] = (a,b)
        else:
            arr[a][b] = (c,d)
    

def dfs(x,y,r,c):
    if visited[x][y]:
        union(x,y,r,c)
        return

    visited[x][y] = True
    arr[x][y] = (r,c)

    if board[x][y] == "U":
        dfs(x-1,y,r,c)
    elif board[x][y] == "D":
        dfs(x+1,y,r,c)
    elif board[x][y] == "L":
        dfs(x,y-1,r,c)
    else:
        dfs(x,y+1,r,c)
        

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i,j,i,j)

cnt = 0
visited = [[False] * m for _ in range(n)]
for r in range(n):
    for c in range(m):
        x, y = find(arr[r][c][0], arr[r][c][1])
        arr[r][c] = (x, y)
        if not visited[x][y]:
            visited[x][y] = True
            cnt += 1
print(cnt)

