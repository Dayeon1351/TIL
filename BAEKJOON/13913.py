from collections import deque
n,k = map(int,input().split())
max_val = 10 ** 5
visited = [-1] * (max_val + 1)
val = [0] * (max_val + 1)

visited[n] = 0
queue = deque([n])
while queue:
    cur_node = queue.popleft()
    if cur_node == k:
        print(visited[cur_node])

        ans = []
        while 1:
            ans.append(str(cur_node))
            if cur_node == n:break
            cur_node = val[cur_node]
        
        print(" ".join(ans[::-1]))
        break

    if 0 <= cur_node * 2 <= max_val and visited[cur_node * 2] == -1:
        visited[cur_node * 2] = visited[cur_node] + 1
        val[cur_node * 2] = cur_node
        queue.append(cur_node * 2)
    
    if 0 <= cur_node - 1 <= max_val and visited[cur_node - 1] == -1:
        visited[cur_node - 1] = visited[cur_node] + 1
        val[cur_node - 1] = cur_node
        queue.append(cur_node - 1)
    
    if 0 <= cur_node + 1 <= max_val and visited[cur_node + 1] == -1:
        visited[cur_node + 1] = visited[cur_node] + 1
        val[cur_node + 1] = cur_node
        queue.append(cur_node + 1)