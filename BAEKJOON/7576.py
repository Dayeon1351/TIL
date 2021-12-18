from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
arr = [list(map(int,input().split()))for i in range(n)]
queue = deque([])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append([i,j])

dx = [0,0,1,-1]
dy = [1,-1,0,0]            

def ripen_tomato():
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                queue.append([nx,ny])
                arr[nx][ny] = arr[a][b] + 1


ripen_tomato()

day = 0
for i in range(n):
    if 0 in arr[i]:
        day = -1
        break
    else:
        day = max(day,max(arr[i]))
else:
    day -= 1

print(day)