from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n = int(input())

def findArea(arr,visited,x,y):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 1
    flag = arr[x][y]

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visited[nx][ny] == 0 and arr[nx][ny] == flag:
                queue.append([nx,ny])
                visited[nx][ny] = 1

    return 0



arr = [list(input().strip())for i in range(n)]
weak_arr = [['B']*n for i in range(n)]

cnt = 0
visited = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            findArea(arr,visited,i,j)
            cnt += 1
        if arr[i][j] != 'B':  
                weak_arr[i][j] = 'R'


weak_cnt = 0
visited = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            findArea(weak_arr,visited,i,j)
            weak_cnt += 1

print(cnt,weak_cnt)