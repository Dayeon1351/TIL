import sys
from collections import defaultdict

input = sys.stdin.readline
n,m,b = map(int,input().split())

dic = defaultdict(int)
for i in range(n):
    for j in list(map(int,input().split())):
        dic[j] += 1

min_val = min(dic.keys())
max_val = max(dic.keys())

height = 0
time = int(1e9)

for h in range(min_val,max_val+1):
    cnt,have = 0,b
    for k in dic.keys():
        if k < h:
            cnt += (h - k) * dic[k]
            have -= (h - k) * dic[k]
        elif h < k:
            cnt += 2 * (k - h) * dic[k]
            have += (k - h) * dic[k]

    if have >= 0:
        time = min(time,cnt)
        if time == cnt:
            height = h

print(time,height)

