from math import gcd
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
k = int(input())

idx = [[(j*10**len(str(arr[i])) + arr[i])% k for j in range(k)]for i in range(n)]

case = 1<<n
dp = [[0]*k for _ in range(case)]
dp[0][0] = 1

for bit in range(case):
    for i in range(n):
        if not bit&(1<<i):
            for j in range(k):
                dp[bit|(1<<i)][idx[i][j]] += dp[bit][j]
            
p = dp[(case)-1][0]
q = sum(dp[(case)-1])
mod = gcd(p,q)
print(p//mod,q//mod,sep="/")