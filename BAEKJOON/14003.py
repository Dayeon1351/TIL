from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int,input().split()))
dp = [0] * (n+1)
num = [-1000000001]
max_val = 0

for i in range(1,n+1):
    if num[-1] < arr[i]:
        num.append(arr[i])
        dp[i] = len(num) - 1
        max_val = dp[i]
    else:
        dp[i] = bisect_left(num,arr[i])
        num[dp[i]] = arr[i]

print(max_val)
result = []
for i in range(n,0,-1):
    if dp[i] == max_val:
        result.append(arr[i])
        max_val -= 1

print(*result[::-1])
