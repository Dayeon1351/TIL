from collections import deque
n,k = map(int,input().split())
max_val = 10 ** 5
cnt = [0] * (max_val+1)

queue = deque([n])
while queue:
    cur_node = queue.popleft()
    if cur_node == k:
        print(cnt[cur_node])
        break
    can_visit = [cur_node-1,cur_node+1,cur_node*2]
    for adj_node in can_visit:
        if 0 <= adj_node <= max_val and not cnt[adj_node]:
            cnt[adj_node] = cnt[cur_node] + 1
            queue.append(adj_node)