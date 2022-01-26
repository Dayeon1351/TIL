import sys
input = sys.stdin.readline

def move_left(board):
    for i in range(n):
        p = 0
        x = 0
        for j in range(n):
            if board[i][j] == 0:
                continue

            if x == 0:
                x = board[i][j]
            else:
                if x == board[i][j]:
                    board[i][p] = x * 2
                    x = 0
                    p += 1
                else:
                    board[i][p] = x
                    x = board[i][j]
                    p += 1

            board[i][j] = 0

        if x != 0:
            board[i][p] = x
    
    return board

def move_right(board):
    for i in range(n):
        p = n-1
        x = 0
        for j in range(n-1,-1,-1):
            if board[i][j] == 0:
                continue
            if x == 0:
                x = board[i][j]
            else:
                if x == board[i][j]:
                    board[i][p] = x * 2
                    x = 0
                    p -= 1
                else:
                    board[i][p] = x
                    x = board[i][j]
                    p -= 1

            board[i][j] = 0

        if x != 0:
            board[i][p] = x
    
    return board

def move_up(board):
    for i in range(n):
        p = 0
        x = 0
        for j in range(n):
            if board[j][i] == 0:
                continue

            if x == 0:
                x = board[j][i]
            else:
                if x == board[j][i]:
                    board[p][i] = x * 2
                    x = 0
                    p += 1
                else:
                    board[p][i] = x
                    x = board[j][i]
                    p += 1

            board[j][i] = 0
        
        if x != 0:
            board[p][i] = x
    
    return board

def move_down(board):
    for i in range(n):
        p = n-1
        x = 0
        for j in range(n-1,-1,-1):
            if board[j][i] == 0:
                continue

            if x == 0:
                x = board[j][i]
            else:
                if x == board[j][i]:
                    board[p][i] = x * 2
                    x = 0
                    p -= 1
                else:
                    board[p][i] = x
                    x = board[j][i]
                    p -= 1

            board[j][i] = 0

        if x != 0:
            board[p][i] = x
    
    return board



def setBlock(arr,cnt):
    global result
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                result = max(result,arr[i][j])
        return
    
    setBlock(move_left([item[:] for item in arr]),cnt+1)
    setBlock(move_right([item[:] for item in arr]),cnt+1)
    setBlock(move_up([item[:] for item in arr]),cnt+1)
    setBlock(move_down([item[:] for item in arr]),cnt+1)
    
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
result = 0
setBlock(arr,0)
print(result)
