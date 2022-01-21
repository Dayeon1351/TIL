from collections import defaultdict
from itertools import combinations
import sys
input = sys.stdin.readline

n,s = map(int,input().split())
arr = tuple(map(int,input().split()))

left_sum = defaultdict(int)
right_sum = defaultdict(int)
left_sum[0] = 1
right_sum[0] = 1
for i in range(1,len(arr[:n//2])+1):
    for left in tuple(combinations(arr[:n//2],i)):
        left_sum[sum(left)] += 1

for i in range(1,len(arr[n//2:])+1):
    for right in tuple(combinations(arr[n//2:],i)):
        right_sum[sum(right)] += 1

left_key = sorted(left_sum.keys())
right_key = sorted(right_sum.keys())

cnt = 0
left_p = 0
right_p = len(right_key) - 1
while left_p < len(left_key) and right_p >= 0:
    num = left_key[left_p] + right_key[right_p]

    if num == s:
        cnt += left_sum[left_key[left_p]] * right_sum[right_key[right_p]] 
        left_p += 1
        right_p -= 1
    elif num > s:
        right_p -= 1
    else:
        left_p += 1

if s == 0:
    cnt -= 1

print(cnt)