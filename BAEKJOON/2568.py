from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort()

dp = [0] * n
num = [0]
max_val = 0

for i in range(n):
    if num[-1] < arr[i][1]:
        num.append(arr[i][1])
        dp[i] = len(num) - 1
        max_val = dp[i]
    else:
        dp[i] = bisect_left(num,arr[i][1])
        num[dp[i]] = arr[i][1]

print(n-max_val)

result = []
for i in range(n-1,-1,-1):
    if dp[i] != max_val:
        result.append(arr[i])
    else:
        max_val -= 1

for i in list(zip(*result[::-1]))[0]:
    print(i)