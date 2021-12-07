import sys
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split())
dic = defaultdict(str)

for i in range(n):
    addr,pw = input().split()
    dic[addr] = pw

for i in range(m):
    print(dic[input().strip()])
