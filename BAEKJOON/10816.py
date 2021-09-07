import sys
from collections import defaultdict
n = int(input())
nums = list(map(int,sys.stdin.readline().split()))
m = int(input())
cards = list(map(int,sys.stdin.readline().split()))

dic = defaultdict(int)
for num in nums:
    dic[num] +=1

for card in cards:
    if card in dic.keys():
        print(dic[card],end=" ")
    else:
        print(0,end=" ")