from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs():
    queue = deque([[0,0]])
    visited[0][0] = True
    key_list = [deque() for _ in range(26)]
    result = 0
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h+2 and 0 <= ny < w+2 and arr[nx][ny] != '*':
                        
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        
                        if arr[nx][ny] == '$':
                            result += 1
                        
                        elif 'A' <= arr[nx][ny] <= 'Z':
                            k = ord(arr[nx][ny]) - ord('A')
                            if not key[k]:
                                key_list[k].append([nx,ny])
                                continue

                        elif 'a'<=arr[nx][ny] <= 'z':
                            k = ord(arr[nx][ny]) - ord('a')
                            key[k] = True
                            while key_list[k]:
                                kx,ky = key_list[k].popleft()
                                queue.append([kx,ky])
                        
                        queue.append([nx,ny])

    return result

t = int(input())
for _ in range(t):
    h,w = map(int,input().split())
    arr = [list('.'*(w+2))] + [list('.'+ input().strip()+'.') for _ in range(h)] + [list('.'*(w+2))]
    visited = [[False]*(w+2) for _ in range(h+2)]
    
    key = [False] * 26
    k = input().strip()
    if k != '0':
        for i in k:
            key[ord(i)-ord('a')] = True
        
    print(bfs())
