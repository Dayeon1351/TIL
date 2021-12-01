import sys
from collections import deque

n = int(input())

queue = deque()
for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == "push_back":
        queue.append(order[1])
    elif order[0] == "push_front":
        queue.appendleft(order[1])
    elif order[0] == "pop_front":
        result = queue.popleft() if queue else -1
        print(result)
    elif order[0] == "pop_back":
        result = queue.pop() if queue else -1
        print(result)
    elif order[0] == "front":
        result = queue[0] if queue else -1
        print(result)
    elif order[0] == "back":
        result = queue[-1] if queue else -1
        print(result)
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        result = 1 if not queue else 0
        print(result)
