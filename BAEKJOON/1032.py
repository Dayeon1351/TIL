import sys
input = sys.stdin.readline

t = int(input())
order = [list(input().strip()) for i in range(t)]

for i in range(t-1):
    for j in range(len(order[i])):
        if order[i][j] != order[i+1][j]:
            order[i+1][j] = '?'

print("".join(order[-1]))