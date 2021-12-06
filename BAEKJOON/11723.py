import sys
input = sys.stdin.readline

n = int(input())
s = set()
default = set(map(str,range(1,21)))
for i in range(n):
    order = input().split()
    if len(order) == 1:
        s = default if order[0] == "all" else set()
    else:
        if (order[0] == "add" or order[0] == "toggle") and order[1] not in s:
            s.add(order[1])
        elif (order[0] == "remove" or order[0] == "toggle") and order[1] in s:
            s.discard(order[1])
        elif order[0] == "check":
            flag = 1 if order[1] in s else 0
            print(flag)