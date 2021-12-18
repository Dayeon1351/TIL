import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int,input().split())
arr = [[list(map(int,input().split()))for i in range(n)]for j in range(h)]

queue = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                queue.append([i,j,k])


dx = [0,0,1,-1]
dy = [1,-1,0,0]
dz = [1,-1]

def ripen_tomato():
    while queue:
        a,b,c = queue.popleft()
        for i in range(2):
            nz = a + dz[i]
            nx = b
            ny = c
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and arr[nz][nx][ny] == 0:
                queue.append([nz,nx,ny])
                arr[nz][nx][ny] = arr[a][b][c] + 1
        
        for i in range(4):
            nz = a 
            nx = b + dx[i]
            ny = c + dy[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and arr[nz][nx][ny] == 0:
                queue.append([nz,nx,ny])
                arr[nz][nx][ny] = arr[a][b][c] + 1
        

ripen_tomato()

day = 0
for j in range(h):
    for i in range(n):
        if 0 in arr[j][i]:
            day = -1
            break
        else:
            day = max(day,max(arr[j][i]))
    else:
        continue
    break
else:
    day -= 1

print(day)