from collections import deque
a,b = map(int,input().split())

queue = deque([[a,1]])
while queue:
    cur_node,cnt = queue.popleft()
    if cur_node == b:
        print(cnt)
        break
    
    if (cur_node * 10) + 1 <= b:
        queue.append([(cur_node * 10) + 1,cnt + 1])

    if cur_node * 2 <= b :
        queue.append([cur_node * 2, cnt + 1])

else:
    print(-1)