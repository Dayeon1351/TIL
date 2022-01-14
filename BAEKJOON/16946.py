from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,list(input().strip()))) for _ in range(n)]
result = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]


for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            result[i][j] = 1


dx = [0,0,-1,1]
dy = [-1,1,0,0]


def getCnt(x,y,num):
    queue = deque([[x,y]])
    visited[x][y] = num
    cnt = 1
    temp = []
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != num:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = num
                    queue.append([nx,ny])
                    cnt += 1
                else:
                    temp.append([nx,ny])
                    visited[nx][ny] = num
    
    for i,j in temp:
        result[i][j] += cnt


idx = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 0:
            getCnt(i,j,idx)
            idx += 1
            
            
for i in range(n):
    for j in range(m):
        print(result[i][j]%10,end="")
    print()
