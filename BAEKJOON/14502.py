from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split()))for i in range(n)]

zero = []
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            zero.append([i,j])
        if arr[i][j] == 2:
            virus.append([i,j])


dx = [0,0,1,-1]
dy = [1,-1,0,0]
def spreadVirus(new_arr):
    queue = deque(virus)
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and new_arr[nx][ny] == 0:
                    new_arr[nx][ny] = 2
                    queue.append([nx,ny])
    
    cnt = 0
    for i in range(n):
        cnt += new_arr[i].count(0)
    return cnt


len_zero = len(zero)
visited = [False] * len_zero
max_val = [0]
def buildWall(idx,m):
    if m == 0:
        new_arr = [item[:] for item in arr]
        num = spreadVirus(new_arr)
        max_val[0] = max_val[0] if max_val[0] > num else num
    else:
        for i in range(idx,len_zero):
            if not visited[i]:
                visited[i] = True
                x,y = zero[i]
                arr[x][y] = 1
                buildWall(i,m-1)
                arr[x][y] = 0
                visited[i] = False
            
buildWall(0,3)
print(max_val[0])