from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
point = [0] * (n+1)

for i in range(1,n+1):
    building = tuple(map(int,input().split()))
    time[i] = building[0]
    for j in building[1:-1]:
        graph[j].append(i)
        point[i] += 1


queue = deque([])
dp = [0] * (n+1)
for i in range(1,n+1):
    if point[i] == 0:
        queue.append(i)
        dp[i] = time[i]

while queue:
    cur_node = queue.popleft()
    for i in graph[cur_node]:
        point[i] -= 1
        dp[i] = max(dp[cur_node]+time[i],dp[i])
        if point[i] == 0:
            queue.append(i)
    
print("\n".join(map(str,dp[1:])))