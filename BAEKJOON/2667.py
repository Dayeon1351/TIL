import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().strip())) for i in range(n)]
visited = [[0]*n for i in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def getBuildingCnt(x,y):
    visited[x][y] = 1
    queue = deque([[x,y]])
    
    cnt = 1
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and arr[nx][ny] == 1:
                    queue.append([nx,ny])
                    visited[nx][ny] = 1
                    cnt += 1
    
    return cnt


result = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and arr[i][j] == 1:
            result.append(getBuildingCnt(i,j))

print(len(result))
print("\n".join(map(str,sorted(result))))