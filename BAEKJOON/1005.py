from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    time = [0] + list(map(int,input().split()))
    graph = [[]for _ in range(n+1)]
    point = [0] * (n+1)
    
    for _ in range(k):
        x,y = map(int,input().split())
        graph[x].append(y)
        point[y] += 1
    w = int(input())

    queue = deque([i for i in range(1,n+1) if point[i] == 0])
    
    dp = [0] + [time[i] if point[i] == 0 else 0 for i in range(1,n+1)]
    
    while queue:
        cur_node = queue.popleft()
        
        for i in graph[cur_node]:
            point[i] -= 1
            dp[i] = max(dp[cur_node] + time[i],dp[i])
            if point[i] == 0:
                queue.append(i)
        
        if cur_node == w:
            print(dp[cur_node])
            break
        

