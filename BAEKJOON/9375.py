from functools import reduce
import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for i in range(t):
    
    n = int(input())
    dic = defaultdict(int)
    
    for j in range(n):
        cloth,kind = input().strip().split()
        dic[kind] += 1

    if len(dic.keys()) == 1:
        print(list(dic.values())[0])
    else:
        clothes = list(dic.values())
        print(reduce(lambda x,y:x*(y+1),clothes,1)-1)




