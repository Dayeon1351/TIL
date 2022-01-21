import sys
input = sys.stdin.readline

n = int(input())
point = [list(map(int,input().split())) for _ in range(n)]
point += [point[0]]

x = 0
y = 0
for i in range(n):
    x += point[i][0] * point[i+1][1]
    y += point[i][1] * point[i+1][0]

print(abs(round((x - y) / 2,1)))