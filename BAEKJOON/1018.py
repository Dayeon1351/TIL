import sys
input = sys.stdin.readline

n,m = map(int,input().split())
chess = [list(input().strip()) for i in range(n)]

ans = []
for row in range(n-7):
    for col in range(m-7):
        idx1 = 0
        idx2 = 0
        for i in range(row,row+8):
            for j in range(col,col+8):
                if (i + j) % 2 == 0:
                    if chess[i][j] != 'W': idx1 += 1
                    if chess[i][j] != 'B': idx2 += 1
                else:
                    if chess[i][j] != 'B': idx1 += 1
                    if chess[i][j] != 'W': idx2 += 1
        ans.append(idx1)
        ans.append(idx2)

print(min(ans))