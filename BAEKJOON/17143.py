import sys
input = sys.stdin.readline

dir = [[-1,0],[1,0],[0,1],[0,-1]]
def outrange(i,j,s,d):

    dx, dy = dir[d-1]
    if d == 1 or d == 2:
        s = s % ((R-1)*2)
    elif d == 3 or d == 4:
        s = s % ((C-1)*2)
    while True:
        if -1 < i+dx*s < R and -1 < j+dy*s < C:
            return (i+dx*s, j+dy*s, d)

        if d == 1:
            s -= i # 가장 위로 만들어주고
            dx, dy = 1, 0 # 방향 바꿔버리기
            i = 0
            d = 2

        elif d == 2: # 가장 아래로 만들어주고
            s -= (R-1-i) 
            dx, dy = -1, 0
            i = R-1
            d = 1
        elif d == 3: # 가장 오른쪽으로 만들고
            s -= (C-1-j)
            dx, dy = 0, -1
            j = C -1
            d = 4
        elif d == 4: # 가장 왼쪽
            s -= j
            dx, dy = 0, 1
            j = 0
            d = 3



R, C, M = map(int,input().split())
board = [[0]*C for _ in range(R)]

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    board[r-1][c-1] = [s,d,z]

result = 0
for j in range(C):
    for i in range(R):
        if board[i][j] != 0:
            result += board[i][j][2]
            board[i][j] = 0
            break

    new_board= [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0: 
                s = board[i][j][0]
                nx, ny, d = outrange(i,j,s,board[i][j][1])
                if new_board[nx][ny] == 0:
                    new_board[nx][ny] = [board[i][j][0],d,board[i][j][2]]

                else:
                    if new_board[nx][ny][2] < board[i][j][2]:
                        new_board[nx][ny] = [board[i][j][0],d,board[i][j][2]]
                            
    board = [item[:] for item in new_board] 


print(result)