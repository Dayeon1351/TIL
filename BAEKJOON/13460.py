from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(input().strip()) for _ in range(n)]
rx,ry = 0,0
bx,by = 0,0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx,ry = i,j
        if arr[i][j] == 'B':
            bx,by = i,j

def move(x,y,dx,dy):
    c = 0
    while arr[x+dx][y+dy] != '#' and arr[x][y] != 'O':
        x += dx
        y += dy
        c += 1
    return x,y,c


dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = [[[[False]*m for _ in range(n)]for _ in range(m)] for _ in range(n)]
queue = deque([[rx,ry,bx,by,1]])
visited[rx][ry][bx][by] = True
def bfs():
    while queue:
        rx,ry,bx,by,cnt = queue.popleft()
        if cnt > 10:
            break

        for i in range(4):
            nx,ny,nc = move(rx,ry,dx[i],dy[i])
            mx,my,mc = move(bx,by,dx[i],dy[i])

            if arr[mx][my] != 'O':
                if arr[nx][ny] == 'O':
                    print(cnt)
                    return

                if nx == mx and ny == my:
                    if nc > mc:
                        nx -= dx[i]
                        ny -= dy[i]
                    else:
                        mx -= dx[i]
                        my -= dy[i]

                if not visited[nx][ny][mx][my]:
                    visited[nx][ny][mx][my] = True
                    queue.append([nx,ny,mx,my,cnt + 1])
    print(-1)

bfs()