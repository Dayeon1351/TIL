import sys
n = int(input())

for i in range(n):
    total = 0
    string = sys.stdin.readline().strip()
    for s in string:
        if s == ')':
            total-=1
        else:
            total+=1
        if total < 0:
            print("NO")
            break
    else:
        if total != 0:
            print("NO")
        else:
            print("YES")
