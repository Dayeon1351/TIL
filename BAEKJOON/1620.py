import sys
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split())

poketmon = defaultdict(int)
for i in range(n):
    poketmon[i+1] = input().strip()

dic = {v:k for k,v in poketmon.items()}

for i in range(m):
    idx = input().strip()
    if not idx.isdigit():
        print(dic[idx])
    else:
        print(poketmon[int(idx)])