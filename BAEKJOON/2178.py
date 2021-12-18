from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().strip()))for i in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = deque([[0,0]])
while queue:
    x,y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
            queue.append([nx,ny])
            arr[nx][ny] = arr[x][y] + 1

print(arr[n-1][m-1])