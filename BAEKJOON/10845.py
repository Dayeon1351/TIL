import sys
n = int(input())
queue = []

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        queue.append(order[1])
    elif order[0] == "pop":
        result = -1 if not queue else queue.pop(0)
        print(result)
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        result = 1 if not queue else 0
        print(result)
    elif order[0] == "front":
        result = -1 if not queue else queue[0]
        print(result)
    elif order[0] == "back":
        result = -1 if not queue else queue[-1]
        print(result)

