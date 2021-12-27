import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[float('INF')]* n for i in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    bus[a-1][b-1] = min(bus[a-1][b-1],c)

for k in range(n):
    bus[k][k] = 0
    for i in range(n):
        for j in range(n):
            bus[i][j] = min(bus[i][j],bus[i][k]+bus[k][j])

for cost in bus:
    for c in cost:
        print(c if c != float('INF') else 0,end=" ")
    print()
