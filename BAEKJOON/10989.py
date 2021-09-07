import sys
from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for i in range(n):
    key = int(sys.stdin.readline())
    dic[key]+=1

for k in sorted(dic.keys()):
    for i in range(dic[k]):
        print(k)
