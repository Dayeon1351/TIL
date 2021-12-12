from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(arr,x,y):
    queue = deque()
    queue.append([x,y])
    arr[x][y] = 0

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append([nx,ny])
    return

t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        x,y = map(int,input().split())
        arr[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(arr,i,j)
                cnt += 1
    print(cnt)