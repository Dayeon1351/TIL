import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

if m:
    btn = input().split()
else:
    btn = []

cnt = abs(100 - n)
for i in range(1000001):
    for j in str(i):
        if j in btn:
            break
    else:
        cnt = min(cnt, len(str(i)) + abs(i-n))

print(cnt)