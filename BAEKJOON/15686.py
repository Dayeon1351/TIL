from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i,j])
        if arr[i][j] == 2:
            chicken.append([i,j])


min_val = float('INF')
for c in combinations(chicken,m):
    sum_val = 0
    for x,y in house:
        sum_val += min([abs(dx-x) + abs(dy-y) for dx,dy in c])
    
    min_val = min(min_val,sum_val)

print(min_val)