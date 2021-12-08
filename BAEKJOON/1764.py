import sys
input = sys.stdin.readline

n, m = map(int,input().split())
no_heard = [input().strip() for i in range(n)]
no_seen = [input().strip() for i in range(m)]

result = list(set(no_heard) & set(no_seen))

print(len(result))
for i in sorted(result):
    print(i)