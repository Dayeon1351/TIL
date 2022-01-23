from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int,input().split())) 
memo = [0]

for i in arr:
    if memo[-1] < i:
        memo.append(i)
    else:
       idx = bisect_left(memo,i)
       memo[idx] = i

print(len(memo)-1)